import json
import yaml


def parse(file_name: str):
    if file_name[-4:] == 'json':
        file = json.load(open(file_name))
    else:
        file = yaml.safe_load(open(file_name))
    return file
