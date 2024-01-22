def to_string(value):
    result = ""
    if isinstance(value, dict):
        result += "[complex value]"
    elif isinstance(value, str):
        result += "\'" + value + "\'"
    else:
        result = value
    return result


def build_path(node):
    name = "'"
    for elem in node:
        key = elem.ger('key')
        type = elem.get('type')
        if type == 'nested':
            name += f"{key}.{build_path(elem['value'])}"
        else:
            name += f"{key}"
    name += "'"
    return name
      

def plain(data):
    string = ""
    for dic in data:
        key = dic["key"]
        type = dic["type"]
        if type == 'added':
            string += f"{key} was added with value: {to_string(dic['value'])}\n"
        elif type == 'deleted':
            string += f"{key} was removed\n"
        elif type == 'changed':
            string += f"{key} was updated. From {to_string(dic['value'][0])} to {to_string(dic['value'][1])}\n"
        elif type == 'unchanged':
            string += f"{key} {to_string(dic['value'])}\n"
        else:
            string += f"{key}{plain(to_string(dic['value']))}\n"
        string = "Property " + string
    return string
