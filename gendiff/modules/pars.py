import json


def pars(file_path: str):
    file = json.load(open(file_path))
    return file
