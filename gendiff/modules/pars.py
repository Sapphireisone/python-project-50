import json
import yaml


def pars(file_path: str):
    if file_path[-4:] == 'json':
        file = json.load(open(file_path))
    else:
        file = yaml.safe_load(open(file_path))
    file = dict(sorted(file.items(), key=lambda x: x[0])) if file else {}
    return file
