import argparse
from gendiff.engine import generate_diff

DESCRIPTION = 'Compares two configuration files and shows a difference.'


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', dest='format', help='format of output')

    
    args = parser.parse_args()
#    print(args.first_file, args.second_file, args.format)

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

if __name__ == '__main__':
    main()
    