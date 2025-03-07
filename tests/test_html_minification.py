from minifier import minify_html
import unittest


class TestHTMLMinification(unittest.TestCase):
    def test_minify_simple_html(self):
        original_html = "<html>   <head><title>Test</title>   </head>   <body> Hello world! <br /></body></html>"
        expected_html = "<html> <head><title>Test</title> </head> <body> Hello world! <br></body></html>"
        self.assertEqual(minify_html(original_html), expected_html)


if __name__ == "__main__":
    unittest.main()
