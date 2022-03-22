from utils import read_files
import sys
import argparse

def test_files(args):

    contents = read_files(args.folder, args.file_name)
    for content in contents:
        print(content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print the contents of a file.')
    parser.add_argument('--folder', '-f', default='web/static/files/', help='Specify the folder directory of the file. (default: web/static/files)')
    parser.add_argument('--file_name', '-fn', help='Specify the name of the file.')
    args = parser.parse_args()

    test_files(args)