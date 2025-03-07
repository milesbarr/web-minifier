import argparse
from pathlib import Path

from . import minify_file, minify_dir


def main() -> None:
    """Command-line interface for minifying web assets."""
    parser = argparse.ArgumentParser(
        prog="minifier",
        description=(
            "Minify web assets by removing unnecessary whitespace, comments, "
            "and other redundant content while preserving functionality."
        ),
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        required=True,
        help="path to input file or directory",
        metavar="PATH",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        required=True,
        help="path to output file or directory",
        metavar="PATH",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="recursively process subdirectories",
    )
    args = parser.parse_args()

    if args.input.is_dir():
        minify_dir(args.input, args.output, recursive=args.recursive)
    else:
        minify_file(args.input, args.output)


if __name__ == "__main__":
    main()
