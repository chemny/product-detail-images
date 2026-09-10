#!/usr/bin/env python3
"""Validate raw aspect ratios and final pixel dimensions without image libraries."""

from __future__ import annotations

import argparse
import struct
import sys
from pathlib import Path


JPEG_SOF = {
    0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
    0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF,
}


def image_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
        if header.startswith(b"\x89PNG\r\n\x1a\n"):
            return struct.unpack(">II", header[16:24])
        if header[:2] != b"\xff\xd8":
            raise ValueError("supported formats are PNG and JPEG")

        handle.seek(2)
        while True:
            byte = handle.read(1)
            if not byte:
                break
            if byte != b"\xff":
                continue
            while byte == b"\xff":
                byte = handle.read(1)
            marker = byte[0]
            if marker in {0xD8, 0xD9}:
                continue
            length_bytes = handle.read(2)
            if len(length_bytes) != 2:
                break
            segment_length = struct.unpack(">H", length_bytes)[0]
            if marker in JPEG_SOF:
                data = handle.read(5)
                if len(data) != 5:
                    break
                height, width = struct.unpack(">HH", data[1:5])
                return width, height
            handle.seek(segment_length - 2, 1)
    raise ValueError("could not read image dimensions")


def parse_pair(value: str, separator: str, label: str) -> tuple[int, int]:
    try:
        first, second = value.lower().split(separator, 1)
        pair = int(first), int(second)
    except (ValueError, AttributeError) as exc:
        raise argparse.ArgumentTypeError(f"{label} must look like 3:4 or 750x1000") from exc
    if pair[0] <= 0 or pair[1] <= 0:
        raise argparse.ArgumentTypeError(f"{label} values must be positive")
    return pair


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--stage", choices=("raw", "final"), required=True)
    parser.add_argument("--ratio", default="3:4")
    parser.add_argument("--pixels")
    parser.add_argument("--tolerance", type=float, default=0.002)
    args = parser.parse_args()

    ratio_w, ratio_h = parse_pair(args.ratio, ":", "ratio")
    expected_ratio = ratio_w / ratio_h
    expected_pixels = parse_pair(args.pixels, "x", "pixels") if args.pixels else None
    if args.stage == "final" and expected_pixels is None:
        parser.error("--pixels is required for --stage final")

    failed = False
    print("file\twidth\theight\tratio\tstatus")
    for path in args.files:
        try:
            width, height = image_size(path)
            actual_ratio = width / height
            ratio_ok = abs(actual_ratio - expected_ratio) <= args.tolerance
            pixels_ok = args.stage == "raw" or (width, height) == expected_pixels
            ok = ratio_ok and pixels_ok
            failed |= not ok
            print(f"{path}\t{width}\t{height}\t{actual_ratio:.6f}\t{'PASS' if ok else 'FAIL'}")
        except (OSError, ValueError) as exc:
            failed = True
            print(f"{path}\t-\t-\t-\tERROR: {exc}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
