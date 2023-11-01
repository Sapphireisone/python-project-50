import json
import yaml


def parse(file_path: str):
    if file_path[-4:] == 'json':
        file = json.load(open(file_path))
    else:
        file = yaml.safe_load(open(file_path))
    return file
