# Minifier

A Python tool for minifying web assets by removing unnecessary whitespace,
comments, and other redundant content while preserving functionality.

## Features

Supports minification of common web file formats:

- HTML (`.html`, `.htm`, `.xhtml`)
- CSS (`.css`)
- JSON (`.json`, `.webmanifest`)
- XML (`.xml`, `.rss`, `.atom`, `.svg`)

All minification preserves full functionality while reducing file size.

## Installation

```bash
# Clone the repository
git clone https://github.com/milesbarr/minifier.git
cd minifier

# Install the package
pip install .
```

## Usage

### Command-Line Interface

Minify a single file:
```bash
python -m minifier -i input.html -o output.html
```

Minify all supported files in a directory:
```bash
python -m minifier -i src/ -o dist/
```

Recursively minify files in a directory and its subdirectories:
```bash
python -m minifier -i src/ -o dist/ -r
```

## License

This project is licensed under the [MIT license](LICENSE).
