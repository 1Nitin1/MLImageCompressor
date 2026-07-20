import argparse

from .compressor import compress_image


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compress an image using KMeans clustering")
    parser.add_argument("input_file", help="Path to the input image file")
    parser.add_argument("--n_colors", type=int, default=50, help="Number of colors to use (default: 50)")
    parser.add_argument("--quality", type=int, default=50, help="JPEG quality from 1 to 95 (default: 50)")
    parser.add_argument("--saveas", default="compressed_image", help="Output filename without extension (default: compressed_image)")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    compress_image(args.input_file, n_colors=args.n_colors, quality=args.quality, saveas=args.saveas)
    print(f"Compressed image saved as {args.saveas}.jpeg")


if __name__ == "__main__":
    main()
