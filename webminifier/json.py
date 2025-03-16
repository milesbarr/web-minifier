import json


def minify_json(s: str) -> str:
    return json.dumps(json.loads(s), separators=(",", ":"))
