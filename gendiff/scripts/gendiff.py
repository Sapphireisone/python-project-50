import argparse
from gendiff.modules.gendiff import generate_diff
from gendiff.modules.make_str import make_str


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration\
 files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    diff = make_str(generate_diff(args.first_file, args.second_file))
    print(diff)


if __name__ == '__main__':
    main()
