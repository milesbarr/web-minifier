import re
from xml.dom import minidom


def minify_xml(s: str) -> str:
    # Parse the XML.
    dom = minidom.parseString(s)

    # Recursively remove unnecessary whitespace and comments.
    def remove_whitespace_and_comments(node: minidom.Node) -> None:
        if node.nodeType in (
            minidom.Node.TEXT_NODE,
            minidom.Node.CDATA_SECTION_NODE,
        ):
            node.data = re.sub(r"\s+", " ", node.data.strip())
        elif node.nodeType == minidom.Node.COMMENT_NODE:
            node.parentNode.removeChild(node)
            return
        for child in list(node.childNodes):
            remove_whitespace_and_comments(child)

    remove_whitespace_and_comments(dom)

    return dom.toxml()
