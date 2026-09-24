#!/usr/bin/env python3
"""Display an ASCII PLY or NumPy point cloud."""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def load_pointcloud(path: str) -> np.ndarray:
    pointcloud_path = Path(path)
    if pointcloud_path.suffix.lower() == ".npy":
        points = np.load(pointcloud_path)
    elif pointcloud_path.suffix.lower() == ".ply":
        points = load_ascii_ply(pointcloud_path)
    else:
        raise ValueError("Input must be a .ply or .npy file")

    points = np.asarray(points, dtype=np.float32)
    if points.ndim != 2 or points.shape[1] < 3:
        raise ValueError(f"Expected point cloud shape (N, 3), got {points.shape}")
    return points[:, :3]


def load_pointcloud_with_colors(path: str) -> tuple[np.ndarray, np.ndarray | None]:
    pointcloud_path = Path(path)
    if pointcloud_path.suffix.lower() == ".ply":
        points, colors = load_ascii_ply_with_colors(pointcloud_path)
        return points, colors
    return load_pointcloud(path), None


def load_ascii_ply(path: Path) -> np.ndarray:
    vertex_count = None
    with path.open("r", encoding="ascii") as file:
        while True:
            line = file.readline()
            if not line:
                raise ValueError("PLY header is missing end_header")
            if line.startswith("element vertex "):
                vertex_count = int(line.split()[2])
            if line.strip() == "end_header":
                break

        if vertex_count is None:
            raise ValueError("PLY header does not contain a vertex count")
        points = [list(map(float, file.readline().split()[:3])) for _ in range(vertex_count)]

    return np.asarray(points, dtype=np.float32)


def load_ascii_ply_with_colors(path: Path) -> tuple[np.ndarray, np.ndarray | None]:
    vertex_count = None
    with path.open("r", encoding="ascii") as file:
        while True:
            line = file.readline()
            if not line:
                raise ValueError("PLY header is missing end_header")
            if line.startswith("element vertex "):
                vertex_count = int(line.split()[2])
            if line.strip() == "end_header":
                break

        if vertex_count is None:
            raise ValueError("PLY header does not contain a vertex count")
        rows = [file.readline().split() for _ in range(vertex_count)]

    points = np.asarray([[float(value) for value in row[:3]] for row in rows], dtype=np.float32)
    colors = None
    if rows and len(rows[0]) >= 6:
        colors = np.asarray([[int(value) for value in row[3:6]] for row in rows], dtype=np.uint8)
    return points, colors


def set_equal_axes(axis, points: np.ndarray):
    minimum = points.min(axis=0)
    maximum = points.max(axis=0)
    center = (minimum + maximum) / 2.0
    radius = max((maximum - minimum).max() / 2.0, 1e-6)
    axis.set_xlim(center[0] - radius, center[0] + radius)
    axis.set_ylim(center[1] - radius, center[1] + radius)
    axis.set_zlim(center[2] - radius, center[2] + radius)


def main():
    parser = argparse.ArgumentParser(description="Display a PLY or NumPy point cloud")
    parser.add_argument("--input", default="output/pointcloud.ply", help="Point cloud path (.ply or .npy)")
    parser.add_argument("--size", type=float, default=1.0, help="Scatter point size")
    args = parser.parse_args()

    points, colors = load_pointcloud_with_colors(args.input)
    figure = plt.figure(figsize=(10, 8))
    axis = figure.add_subplot(111, projection="3d")
    if colors is None:
        axis.scatter(points[:, 0], points[:, 1], points[:, 2], s=args.size, c=points[:, 2], cmap="viridis")
    else:
        axis.scatter(points[:, 0], points[:, 1], points[:, 2], s=args.size, c=colors / 255.0)
    axis.set_xlabel("X")
    axis.set_ylabel("Y")
    axis.set_zlabel("Z")
    axis.set_title(f"Point cloud: {Path(args.input).name} ({len(points):,} points)")
    set_equal_axes(axis, points)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()