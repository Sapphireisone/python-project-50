from gendiff.formats.stylish import stylish
from gendiff.formats.plain import plain
from gendiff.formats.json import to_json


def format(tree, output_format='stylish'):
    formats = {'stylish': stylish, 'plain': plain, 'json': to_json}
    if output_format in formats:
        return formats[output_format](tree)
    raise ValueError(f'\nUnknown format: {output_format}')