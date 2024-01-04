def stylish(in_data, depth=1, result='{\n', end='}'):
    shift = "  " + ("  " * depth)
    for dictionary in in_data:
        key = dictionary["key"]
        value = dictionary["value"]
        type = dictionary["type"]
        if type == "added":
            result += f"{shift}+ {key}: {value}\n"
        elif type == "deleted":
            result += f"{shift}- {key}: {value}\n"
        elif type == "changed":
            result += f"{shift}- {key}: {value[0]}\n"
            result += f"{shift}+ {key}: {value[1]}\n"
        elif type == "unchanged":
            result += f"{shift}  {key}: {value}\n"
        else:
            result += shift + key + ": {\n"
            result += f"{stylish(value, depth + 1, result='', end=' ')}\n"
            result += shift + "}\n"

    result += end
    return result 
