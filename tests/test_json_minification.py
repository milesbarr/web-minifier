import unittest

from webminifier import minify_json


class TestJSONMinification(unittest.TestCase):
    def test_minify_json(self):
        original_json = """
        {
            "name": "John Doe",
            "age": 30,
            "is_active": true,
            "skills": [
                "Python",
                "JavaScript"
            ],
            "address": {
                "street": "123 Main St",
                "city": "Anytown"
            }
        }
        """
        expected_json = (
            '{"name":"John Doe","age":30,"is_active":true,"skills":["Python","'
            'JavaScript"],"address":{"street":"123 Main St","city":"Anytown"}}'
        )
        self.assertEqual(minify_json(original_json), expected_json)


if __name__ == "__main__":
    unittest.main()
