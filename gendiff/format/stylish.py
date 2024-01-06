def stringer(value, depth=0):
    shift = ("    " * depth) + "    "
    result = ""
    if isinstance(value, dict):
        result += "{\n"
        for key, val in value.items():
            result += f"{shift}{shift}{key}: {stringer(val, depth+1)}\n"
        result += shift + "}"
    else:
        result = value
    return result


def stylish(data, depth=0, result='{\n', end='}'):
    shift = ("    " * depth) + "  "
    for dic in data:
        key = dic["key"]
        type = dic["type"]
        if type == "added":
            result += f"{shift}+ {key}: {stringer(dic['value'])}\n"
        elif type == "deleted":
            result += f"{shift}- {key}: {stringer(dic['value'])}\n"
        elif type == "changed":
            result += f"{shift}- {key}: {stringer(dic['value'][0])}\n"
            result += f"{shift}+ {key}: {stringer(dic['value'][1])}\n"
        elif type == "unchanged":
            result += f"{shift}  {key}: {stringer(dic['value'])}\n"
        else:
            result += f"{shift}  {key}" + ": {\n"
            result += f"{stylish(stringer(dic['value']), depth + 1, result='', end=' ')}\n"
            result += shift + "  }\n"
    return result + end
