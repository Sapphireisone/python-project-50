from gendiff.modules.parse import parse


def generate_diff(file_path1, file_path2):
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    file1 = dict(sorted(file1.items(), key=lambda x: x[0])) if file1 else {}
    file2 = dict(sorted(file2.items(), key=lambda x: x[0])) if file2 else {}
    result = {}
    for key in file1:
        if key not in file2:
            result[f'- {key}'] = file1[key]
        else:
            if file1.get(key) == file2.get(key):
                result[f'  {key}'] = file1[key]
            else:
                result[f'- {key}'] = file1[key]
                result[f'+ {key}'] = file2[key]
    for key in file2:
        if key not in file1:
            result[f'+ {key}'] = file2[key]
    return result
