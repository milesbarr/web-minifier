from minifier import minify_css
import unittest


class TestCSSMinification(unittest.TestCase):
    def test_minify_css(self):
        original_css = """
        body {
            background-color: #ffffff;
            color: black;
            margin: 0px;
            padding: 0px;
        }
        /* Comment */
        .class {
            font-size: 1em; 
            width: 100%;
        }
        """
        expected_css = "body{background-color:#fff;color:#000;margin:0px;padding:0px} .class{font-size:1em;width:100%}"
        self.assertEqual(minify_css(original_css), expected_css)


if __name__ == "__main__":
    unittest.main()
