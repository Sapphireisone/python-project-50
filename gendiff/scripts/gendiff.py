import argparse
# from gendiff.modules.generate_diff import generate_diff, FILE1, FILE2
# from gendiff.modules.make_to_string import make_to_string


parser = argparse.ArgumentParser(description='Compares two configuration\
 files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def main():
    pass


if __name__ == '__main__':
    main()
