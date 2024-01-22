from gendiff.modules.parser import parse
from gendiff.modules.tree import tree
from gendiff.modules.formater import format


def gendiff(file1, file2, output_format='stylish'):
    first_file = parse(file1)
    second_file = parse(file2)
    diff = tree(first_file, second_file)
    result = format(diff, output_format)
    return result
