import os
from pathlib import Path
from typing import Optional

from .css import minify_css
from .html import minify_html
from .json import minify_json
from .xml import minify_xml


__all__ = [
    "minify_css",
    "minify_html",
    "minify_json",
    "minify_xml",
    "minify_file",
    "minify_dir",
]

_MINIFY_BY_EXTENSION = {
    ".atom": minify_xml,
    ".css": minify_css,
    ".htm": minify_html,
    ".html": minify_html,
    ".json": minify_json,
    ".rss": minify_xml,
    ".svg": minify_xml,
    ".webmanifest": minify_json,
    ".xhtml": minify_html,
    ".xml": minify_xml,
}


def minify_file(
    input_path: str | bytes | os.PathLike,
    output_path: str | bytes | os.PathLike,
) -> None:
    """Minify a single file based on its extension.

    Args:
        input_path: Path to the input file
        output_path: Path where the minified content will be written
        verbose: If True, print processing information

    Raises:
        ValueError: If the file extension is not supported
        IOError: If there are issues reading or writing files
    """
    input_path = Path(input_path)
    output_path = Path(output_path)

    minify = _MINIFY_BY_EXTENSION.get(input_path.suffix.lower())
    if not minify:
        raise ValueError(f"Unsupported file extension: {input_path.suffix}")

    with input_path.open("r", encoding="utf-8") as f:
        content = f.read()
    content = minify(content)
    with output_path.open("w", encoding="utf-8") as f:
        f.write(content)


def minify_dir(
    input_dir: str | bytes | os.PathLike,
    output_dir: str | bytes | os.PathLike,
    recursive: bool = False,
) -> None:
    """Minify all supported files in a directory.

    Args:
        input_dir: Path to the input directory
        output_dir: Path to the output directory
        recursive: If True, process subdirectories recursively

    Raises:
        NotADirectoryError: If input_dir is not a directory
        IOError: If there are issues reading or writing files
    """
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)

    if not input_dir.is_dir():
        raise NotADirectoryError(f"Input path is not a directory: {input_dir}")

    pattern = "**/*" if recursive else "*"
    for input_path in input_dir.glob(pattern):
        if not input_path.is_file():
            continue
        if input_path.suffix.lower() not in _MINIFY_BY_EXTENSION:
            continue
        rel_path = input_path.relative_to(input_dir)
        output_path = output_dir / rel_path
        output_path.parent.mkdir(exist_ok=True)
        minify_file(input_path, output_path)
