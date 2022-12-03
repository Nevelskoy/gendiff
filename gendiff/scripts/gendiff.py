'''Main module'''

import argparse
from gendiff.engine import generate_diff


DESCRIPTION = 'Compares two configuration files and shows a difference.'
HELP = 'set format of output'


def main():
    '''Get difference between two files.
    Returns:
        str: description of files differences
    '''
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', dest='format', help=HELP)

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
