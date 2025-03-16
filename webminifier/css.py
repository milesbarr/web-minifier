import re

# https://developer.mozilla.org/en-US/docs/Web/CSS/named-color
_CSS_NAMED_COLORS = {
    "black": "#000",
    "white": "#fff",
    "red": "#f00",
    "fuchsia": "#f0f",
    "lime": "#0f0",
    "yellow": "#ff0",
    "blue": "#00f",
    "aqua": "#0ff",
}


def minify_css(s: str) -> str:
    # Remove comments.
    s = re.sub(r"\/\*[^*]*\*+([^/*][^*]*\*+)*\/", "", s, flags=re.DOTALL)

    # Remove whitespace around symbols.
    s = re.sub(r"\s*([{\[\]:;,])\s*", r"\1", s)
    s = re.sub(r"\s*}", "}", s)

    # Collapse whitespace.
    s = re.sub(r"\s+", " ", s).strip()

    # Remove the last semicolons in style definitions.
    s = s.replace(";}", "}")

    # Use shorthand hex colors.
    s = re.sub(
        r"#([a-fA-F0-9])\1([a-fA-F0-9])\2([a-fA-F0-9])\3\b", r"#\1\2\3", s
    )

    # Replace named colors with hex equivalents.
    for name, hex in _CSS_NAMED_COLORS.items():
        s = re.sub(rf"\b{name}\b", hex, s, flags=re.IGNORECASE)

    return s
