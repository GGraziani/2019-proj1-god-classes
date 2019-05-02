import sys
import argparse
from utils.doc_utils import *


# add one gateway function for each functionality
def find_god_classes_gateway(args):
    from pre_processing import find_god_classes
    print(find_god_classes.find_god_classes_argparse(args))


def extract_feature_vectors_gateway(args):
    from pre_processing import extract_feature_vectors
    extract_feature_vectors.extract_feature_vectors_argparse(args)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# add parser for find_god_classes
p_find_god_classes = subparsers.add_parser('find_god_classes')
p_find_god_classes.add_argument('-s', '-src', '--source', dest='source', default=None)
p_find_god_classes.set_defaults(func=find_god_classes_gateway)

# add parser for extract_feature_vectors
p_extract_feature_vectors = subparsers.add_parser('extract_feature_vectors')
p_extract_feature_vectors.add_argument('-s', '-src', '--source', dest='source', default=None)
p_extract_feature_vectors.set_defaults(func=extract_feature_vectors_gateway)


def main(argv):

    helpstrings = {'', '-h', '--help'}

    command = listget(argv, 0, '').lower()
    print('command = "%s"' % command)

    # The user did not enter a command, or the entered command is not recognized.
    if command not in MODULE_DOCSTRINGS:
        print(DOCSTRING)
        if command == '':
            print('You are seeing the default help text because you did not choose a command.')
        elif command not in helpstrings:
            print('You are seeing the default help text because "%s" was not recognized' % command)
        return 1

    # The user entered a command, but no further arguments, or just help.
    argument = listget(argv, 1, '').lower()
    print('argument = "%s"' % argument)
    if argument in helpstrings:
        print(MODULE_DOCSTRINGS[command])
        return 1

    args = parser.parse_args(argv)
    args.func(args)

    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
