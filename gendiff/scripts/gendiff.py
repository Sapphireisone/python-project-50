import argparse
from gendiff.modules.gendiff import generate_diff
from gendiff.format.stylish import stylish
from gendiff.modules.parse import parse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration\
 files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file1 = parse(args.first_file)
    file2 = parse(args.second_file)
    diff = generate_diff(file1, file2)
    result = stylish(diff)
    print(result)


if __name__ == '__main__':
    main()
