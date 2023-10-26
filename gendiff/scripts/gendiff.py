import argparse
from gendiff.modules.gendiff import generate_diff


parser = argparse.ArgumentParser(description='Compares two configuration\
 files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def main():
    dif = generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json')
    print(dif)


if __name__ == '__main__':
    main()
