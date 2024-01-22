import argparse
from gendiff.modules.gendiff import gendiff


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration\
 files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    output_format = args.format
    print(gendiff(first_file, second_file, output_format))


if __name__ == '__main__':
    main()
