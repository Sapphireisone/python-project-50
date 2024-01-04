def get_type(dic):
    if dic.get('type') == 'added':
        result = '+ '
    elif dic.get('type') == 'deleted':
        result = '- '
    else:
        result = '  '
    return result


def stylish(inData, depth=1):
    result = "{\n"
    for dictionary in inData:
        shift = "  " * depth
        if "value" in dictionary:
            if type(dictionary["value"]) is not list:
                key = str(dictionary["key"])
                value = str(dictionary["value"])  
                result += f'{shift}{get_type(dictionary)}{key}: {value}\n'
            else:
                for itemList in dictionary["value"]:
                    stylish(itemList, depth + 1)
        if "value1" in dictionary:
            if type(dictionary["value1"]) is not list:
                key = str(dictionary["key"])
                value1 = str(dictionary["value1"])
                value2 = str(dictionary["value2"])  
                result += f'{shift}- {key}: {value1}\n'
                result += f'{shift}+ {key}: {value2}\n'
            else:
                for itemList in dictionary["value1"]:
                    stylish(itemList, depth + 1)
                for itemList in dictionary["value2"]:
                    stylish(itemList, depth + 1)
    result += "}"
    return result
