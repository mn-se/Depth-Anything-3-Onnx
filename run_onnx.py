#!/usr/bin/env python3
"""
Run Depth Anything 3 using an ONNX model.

Mirrors the PyTorch pipeline:
    - fixed-square preprocessing (default 504)
    - visualization with matplotlib (optional)
    - depth_vis export resized back to the original image size

Example:
    python run_onnx.py --image input.jpg --visualize --export-dir ./output --onnx DA3-SMALL-504.onnx
"""

import argparse
import json
import os
import sys
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np
import onnxruntime as ort
from PIL import Image

# Ensure local package import works when running from repo root
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from depth_anything_3.utils.io.input_processor import InputProcessor
from depth_anything_3.utils.visualize import visualize_depth


def parse_args():
    parser = argparse.ArgumentParser(description="Run Depth Anything 3 (ONNX)")
    parser.add_argument(
        "--image",
        type=str,
        default="assets/examples/SOH/000.png",
        help="Path to input image or directory",
    )
    parser.add_argument(
        "--camera",
        type=int,
        default=None,
        help="Camera device number. When set, capture one frame instead of using --image",
    )
    parser.add_argument(
        "--onnx",
        type=str,
        default="DA3-SMALL-504.onnx",
        help="Path to ONNX model",
    )
    parser.add_argument(
        "--process-res",
        type=int,
        default=504,
        help="Fixed square processing resolution",
    )
    parser.add_argument(
        "--export-dir",
        type=str,
        default=None,
        help="Directory to export depth_vis images",
    )
    parser.add_argument(
        "--visualize",
        action="store_true",
        help="Show visualization (requires display)",
    )
    parser.add_argument(
        "--calibration",
        type=str,
        default="calib_data/result.json",
        help="Camera calibration JSON path. Use an empty value to disable undistortion",
    )
    parser.add_argument(
        "--pointcloud-output",
        type=str,
        default=None,
        help="Export the inferred depth as a PLY point cloud",
    )
    parser.add_argument(
        "--pointcloud-downsample",
        type=int,
        default=8,
        help="Point cloud downsample factor",
    )
    return parser.parse_args()


def get_orig_hw(image: str | np.ndarray) -> tuple[int, int]:
    if isinstance(image, np.ndarray):
        height, width = image.shape[:2]
        return height, width

    with Image.open(image) as im:
        w, h = im.size
    return h, w


def load_calibration(calibration_path: str, width: int, height: int):
    if not calibration_path:
        return None

    with Path(calibration_path).open("r", encoding="utf-8") as f:
        calibration = json.load(f)

    camera_matrix = calibration["camera_matrix"]
    calibration_size = calibration["image_size"]
    scale_x = width / calibration_size["width"]
    scale_y = height / calibration_size["height"]
    matrix = np.array(
        [
            [camera_matrix["fx"] * scale_x, 0.0, camera_matrix["cx"] * scale_x],
            [0.0, camera_matrix["fy"] * scale_y, camera_matrix["cy"] * scale_y],
            [0.0, 0.0, 1.0],
        ],
        dtype=np.float32,
    )
    distortion = calibration.get("distortion")
    if distortion is None:
        return matrix, None

    coefficients = np.array(
        [distortion["k1"], distortion["k2"], distortion["p1"], distortion["p2"], distortion["k3"]],
        dtype=np.float32,
    )
    return matrix, coefficients


def preprocess_image(image: str | np.ndarray, process_res: int, calibration_path: str = ""):
    image_input = image
    if isinstance(image, np.ndarray):
        image_input = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if calibration_path:
        image_bgr = cv2.imread(image) if isinstance(image, str) else image
        if image_bgr is None:
            raise FileNotFoundError(f"Could not read image: {image}")
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB) if isinstance(image, str) else image_input
        height, width = image_rgb.shape[:2]
        camera_matrix, distortion = load_calibration(calibration_path, width, height)
        if distortion is not None:
            image_input = cv2.undistort(image_rgb, camera_matrix, distortion)
        else:
            image_input = image_rgb

    ip = InputProcessor()
    imgs_cpu, _, _ = ip(
        image=[image_input],
        process_res=process_res,
        process_res_method="fixed_square",
        num_workers=1,
        sequential=True,
    )
    # imgs_cpu: (1, N=1, 3, H, W); take first image -> (3, H, W)
    img = imgs_cpu[0]
    orig_hw = get_orig_hw(image)
    return img, orig_hw


def run_onnx(
    model_path: str,
    image: str | np.ndarray,
    process_res: int,
    calibration_path: str = "",
):
    print("Loading ONNX model: {}".format(model_path))
    sess = ort.InferenceSession(
        model_path,
        providers=["CPUExecutionProvider"],
    )

    img, orig_hw = preprocess_image(image, process_res, calibration_path)
    input_image = img.unsqueeze(0).numpy()  # (1, 3, H, W)

    print("Running ONNX inference")
    outputs = sess.run(None, {"image": input_image})
    depth = outputs[0]  # expect (1, 1, H, W) or (1, H, W)
    depth = np.array(depth)
    if depth.ndim == 4:
        depth = depth[0, 0]
    elif depth.ndim == 3:
        depth = depth[0]

    # Resize depth back to original resolution
    target_h, target_w = orig_hw
    if depth.shape != (target_h, target_w):
        depth = cv2.resize(depth, (int(target_w), int(target_h)), interpolation=cv2.INTER_LINEAR)

    return depth, orig_hw


def save_depth_vis(depth: np.ndarray, export_dir: str, index: int = 0):
    os.makedirs(os.path.join(export_dir, "depth_vis"), exist_ok=True)
    depth_vis = visualize_depth(depth).astype(np.uint8)
    save_path = os.path.join(export_dir, f"depth_vis/{index:04d}.jpg")
    import imageio

    imageio.imwrite(save_path, depth_vis, quality=95)
    return save_path


def save_pointcloud(
    depth: np.ndarray,
    image: str | np.ndarray,
    output_path: str,
    calibration_path: str,
    orig_hw: tuple[int, int],
    step: int,
):
    from depth_to_pointcloud import (
        depth_to_pointcloud,
        estimate_intrinsics,
        load_calibration,
        sample_pointcloud_colors,
        save_ply,
    )

    height, width = orig_hw
    calibration = load_calibration(calibration_path, width, height)
    if calibration is None:
        fx, fy, cx, cy = estimate_intrinsics(width, height)
    else:
        (fx, fy, cx, cy), _ = calibration

    points = depth_to_pointcloud(depth, fx, fy, cx, cy, step=step, distortion=None)
    image_bgr = cv2.imread(image) if isinstance(image, str) else image
    if image_bgr is None:
        raise FileNotFoundError(f"Could not read image: {image}")
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    if calibration_path:
        _, distortion = load_calibration(calibration_path, width, height)
        if distortion is not None:
            image_rgb = cv2.undistort(image_rgb, np.array([[fx, 0.0, cx], [0.0, fy, cy], [0.0, 0.0, 1.0]], dtype=np.float32), distortion)
    colors = sample_pointcloud_colors(depth, image_rgb, step=step)
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    np.save(str(output.with_suffix(".npy")), points)
    save_ply(points, str(output), colors)
    return output, output.with_suffix(".npy"), len(points)


def main():
    args = parse_args()

    camera = None
    if args.camera is not None:
        camera = cv2.VideoCapture(args.camera)
        if not camera.isOpened():
            raise RuntimeError(f"Could not open camera device {args.camera}")
        try:
            success, frame = camera.read()
        finally:
            camera.release()
        if not success:
            raise RuntimeError(f"Could not capture a frame from camera device {args.camera}")
        input_image = frame
        print(f"Using camera device: {args.camera}")
        if args.export_dir:
            os.makedirs(args.export_dir, exist_ok=True)
            captured_path = os.path.join(args.export_dir, f"camera_{args.camera}_input.jpg")
            cv2.imwrite(captured_path, frame)
            print(f"  - Captured frame saved to: {captured_path}")
    else:
        input_image = args.image

    depth, orig_hw = run_onnx(args.onnx, input_image, args.process_res, args.calibration)
    print("[OK] Inference complete. Depth shape (original scale): {}".format(depth.shape))

    if args.export_dir:
        saved = save_depth_vis(depth, args.export_dir, index=0)
        print("  - Saved depth visualization to: {}".format(saved))

    if args.pointcloud_output:
        if args.pointcloud_downsample <= 0:
            raise ValueError("--pointcloud-downsample must be >= 1")
        ply_path, npy_path, point_count = save_pointcloud(
            depth,
            input_image,
            args.pointcloud_output,
            args.calibration,
            orig_hw,
            args.pointcloud_downsample,
        )
        print(f"  - Point cloud saved to: {ply_path}")
        print(f"  - Numpy point cloud saved to: {npy_path}")
        print(f"  - Point count: {point_count}")

    if args.visualize:
        print("\nGenerating visualization...")
        depth_vis = visualize_depth(depth)
        fig, ax = plt.subplots(1, 1, figsize=(8, 6))
        ax.imshow(depth_vis)
        ax.set_title("Depth")
        ax.axis("off")
        plt.tight_layout()
        plt.show()
        print("[OK] Visualization complete!")


if __name__ == "__main__":
    main()

