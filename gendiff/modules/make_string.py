def make_string(diff):
    result = '{'
    if diff:
        result += '\n'
        for el in diff:
            if el[0] == '-' or el[0] == '+':
                result += f' {el}: {diff[el]}\n'
            else:
                result += f'   {el}: {diff[el]}\n'
    result += '}'
    return result
