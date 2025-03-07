from minifier import minify_xml
import unittest


class TestXMLMinification(unittest.TestCase):
    def test_minify_xml(self):
        original_xml = """
        <root>
            <!-- This is a comment -->
            <child>
                Text with    unnecessary   spaces
            </child>
            <child>
                More text
            </child>
            <!-- Another comment -->
        </root>
        """
        expected_xml = '<?xml version="1.0" ?><root><child>Text with unnecessary spaces</child><child>More text</child></root>'
        self.assertEqual(minify_xml(original_xml), expected_xml)


if __name__ == "__main__":
    unittest.main()
