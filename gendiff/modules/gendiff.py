from gendiff.modules.make_string import make_string
from gendiff.modules.pars import pars


def generate_diff(file_path1: str, file_path2: str):
    file1 = pars(file_path1)
    file2 = pars(file_path2)
    file1 = dict(sorted(file1.items(), key=lambda x: x[0]))
    file2 = dict(sorted(file2.items(), key=lambda x: x[0]))
    result = {}
    for key in file1:
        if key not in file2:
            result[f'- {key}'] = file1[key]
        else:
            if file1.get(key) == file2.get(key):
                result[f'{key}'] = file1[key]
            else:
                result[f'- {key}'] = file1[key]
                result[f'+ {key}'] = file2[key]
    for key in file2:
        if key not in file1:
            result[f'+ {key}'] = file2[key]
    dif = make_string(result)
    return dif