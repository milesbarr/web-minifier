import re

from bs4 import BeautifulSoup, Comment

from webminifier.css import minify_css
from webminifier.json import minify_json


def minify_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # Remove comments.
    for comment in soup.find_all(string=lambda s: isinstance(s, Comment)):
        comment.extract()

    # Minify CSS within style tags.
    for style in soup.find_all("style"):
        style.string.replace_with(minify_css(style.string))

    # Minify JSON-LD within script tags.
    for script in soup.find_all("script", type="application/ld+json"):
        script.string.replace_with(minify_json(script.string))

    # Convert to a string.
    html = soup.encode(formatter="html5").decode()

    # Collapse whitespace.
    html = re.sub(r"\s+", " ", html)

    return html
