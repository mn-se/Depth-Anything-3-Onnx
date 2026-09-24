#!/usr/bin/env python3
"""
Convert a Depth Anything 3 depth map to a 3D point cloud.

Example:
    uv run python depth_to_pointcloud.py \
        --image assets/examples/input.jpg \
        --onnx DA3-SMALL-504.onnx \
        --process-res 504 \
        --output output/pointcloud.ply \
        --downsample 8
"""

import argparse
import json
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from run_onnx import run_onnx


def parse_args():
    parser = argparse.ArgumentParser(description="Convert a depth map to a 3D point cloud")
    parser.add_argument("--image", type=str, default="assets/examples/input.jpg", help="Input image path")
    parser.add_argument("--onnx", type=str, default="DA3-SMALL-504.onnx", help="ONNX model path")
    parser.add_argument("--process-res", type=int, default=504, help="Square processing resolution")
    parser.add_argument("--output", type=str, default="output/pointcloud.ply", help="Output PLY path")
    parser.add_argument("--downsample", type=int, default=8, help="Downsample factor for point cloud export")
    parser.add_argument(
        "--calibration",
        type=str,
        default="calib_data/result.json",
        help="Camera calibration JSON path. Use an empty value to disable it",
    )
    parser.add_argument("--fx", type=float, default=None, help="Override camera focal length in x direction")
    parser.add_argument("--fy", type=float, default=None, help="Override camera focal length in y direction")
    parser.add_argument("--cx", type=float, default=None, help="Override principal point x")
    parser.add_argument("--cy", type=float, default=None, help="Override principal point y")
    return parser.parse_args()


def estimate_intrinsics(width: int, height: int):
    # Reasonable fallback when no camera calibration is available.
    # This is not physically exact for all cameras, but it makes the point cloud usable.
    focal = 0.8 * max(width, height)
    return focal, focal, width / 2.0, height / 2.0


def load_calibration(calibration_path: str, width: int, height: int):
    if not calibration_path:
        return None

    with Path(calibration_path).open("r", encoding="utf-8") as f:
        calibration = json.load(f)

    camera_matrix = calibration["camera_matrix"]
    calibration_size = calibration["image_size"]
    scale_x = width / calibration_size["width"]
    scale_y = height / calibration_size["height"]
    intrinsics = (
        camera_matrix["fx"] * scale_x,
        camera_matrix["fy"] * scale_y,
        camera_matrix["cx"] * scale_x,
        camera_matrix["cy"] * scale_y,
    )
    distortion = calibration.get("distortion")
    if distortion is not None:
        distortion = np.array(
            [distortion["k1"], distortion["k2"], distortion["p1"], distortion["p2"], distortion["k3"]],
            dtype=np.float32,
        )
    return intrinsics, distortion


def depth_to_pointcloud(
    depth: np.ndarray,
    fx: float,
    fy: float,
    cx: float,
    cy: float,
    step: int = 1,
    distortion: np.ndarray | None = None,
):
    h, w = depth.shape
    yy, xx = np.indices((h, w), dtype=np.float32)
    yy = yy[::step, ::step]
    xx = xx[::step, ::step]
    z = depth[::step, ::step].astype(np.float32)

    if distortion is not None:
        pixels = np.column_stack((xx.ravel(), yy.ravel())).astype(np.float32)
        camera_matrix = np.array([[fx, 0.0, cx], [0.0, fy, cy], [0.0, 0.0, 1.0]], dtype=np.float32)
        undistorted = cv2.undistortPoints(pixels.reshape(-1, 1, 2), camera_matrix, distortion).reshape(xx.shape + (2,))
        x_ray = undistorted[..., 0]
        y_ray = undistorted[..., 1]
    else:
        x_ray = (xx - cx) / fx
        y_ray = (yy - cy) / fy

    valid = np.isfinite(z) & (z > 0)
    x = np.zeros_like(z, dtype=np.float32)
    y = np.zeros_like(z, dtype=np.float32)
    x[valid] = x_ray[valid] * z[valid]
    y[valid] = y_ray[valid] * z[valid]

    points = np.column_stack((x[valid], y[valid], z[valid])).astype(np.float32)
    return points


def sample_pointcloud_colors(depth: np.ndarray, image_rgb: np.ndarray, step: int = 1):
    if image_rgb.shape[:2] != depth.shape:
        raise ValueError(f"Image and depth sizes must match, got {image_rgb.shape[:2]} and {depth.shape}")

    z = depth[::step, ::step]
    colors = image_rgb[::step, ::step, :3]
    valid = np.isfinite(z) & (z > 0)
    return colors[valid].astype(np.uint8)


def save_ply(points: np.ndarray, output_path: str, colors: np.ndarray | None = None):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if colors is not None and len(colors) != len(points):
        raise ValueError("Colors and points must contain the same number of entries")

    with output_path.open("w", encoding="utf-8") as f:
        f.write("ply\n")
        f.write("format ascii 1.0\n")
        f.write(f"element vertex {len(points)}\n")
        f.write("property float x\n")
        f.write("property float y\n")
        f.write("property float z\n")
        if colors is not None:
            f.write("property uchar red\n")
            f.write("property uchar green\n")
            f.write("property uchar blue\n")
        f.write("end_header\n")
        if colors is None:
            for p in points:
                f.write(f"{p[0]:.6f} {p[1]:.6f} {p[2]:.6f}\n")
        else:
            for p, color in zip(points, colors):
                f.write(f"{p[0]:.6f} {p[1]:.6f} {p[2]:.6f} {color[0]} {color[1]} {color[2]}\n")


def main():
    args = parse_args()

    # Run inference to get the depth map in original image resolution.
    depth, orig_hw = run_onnx(args.onnx, args.image, args.process_res, calibration_path="")
    h, w = orig_hw

    calibration = load_calibration(args.calibration, w, h)
    if calibration is None:
        fx, fy, cx, cy = estimate_intrinsics(w, h)
        distortion = None
    else:
        (fx, fy, cx, cy), distortion = calibration

    fx = args.fx if args.fx is not None else fx
    fy = args.fy if args.fy is not None else fy
    cx = args.cx if args.cx is not None else cx
    cy = args.cy if args.cy is not None else cy

    if args.downsample <= 0:
        raise ValueError("--downsample must be >= 1")

    points = depth_to_pointcloud(depth, fx, fy, cx, cy, step=args.downsample, distortion=distortion)
    image = cv2.imread(args.image)
    if image is None:
        raise FileNotFoundError(f"Could not read image: {args.image}")
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    colors = sample_pointcloud_colors(depth, image_rgb, step=args.downsample)
    np.save(str(Path(args.output).with_suffix(".npy")), points)
    save_ply(points, args.output, colors)

    print(f"Point cloud saved to: {args.output}")
    print(f"Numpy array saved to: {Path(args.output).with_suffix('.npy')}")
    print(f"Point count: {len(points)}")
    print("Coordinate convention: x = right, y = down, z = depth")
    print(f"Camera calibration: {args.calibration or 'disabled'}")


if __name__ == "__main__":
    main()
