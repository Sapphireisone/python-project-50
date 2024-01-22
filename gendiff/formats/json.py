import json


def to_json(tree):
    return json.dumps(tree, indent=4)