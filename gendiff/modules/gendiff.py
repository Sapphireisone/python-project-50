from gendiff.modules.pars import pars


def generate_diff(file_path1, file_path2):
    file1 = pars(file_path1)
    file2 = pars(file_path2)
    result = '{\n'
    for key in file1:
        if key not in file2:
            result += f' - {key}: {file1[key]}\n'
        else:
            if file1.get(key) == file2.get(key):
                result += f'   {key}: {file1[key]}\n'
            else:
                result += f' - {key}: {file1[key]}\n'
                result += f' + {key}: {file2[key]}\n'
    for key in file2:
        if key not in file1:
            result += f' + {key}: {file2[key]}\n'
    result += '}'
    result = '{}' if result == '{\n}' else result
    return result
