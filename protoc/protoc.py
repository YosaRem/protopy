from FileGenerator import FileGenerator
import argparse


def main():
    parser = argparse.ArgumentParser(description="Proto compile")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p", "--python_in", help="Proto file that will convert to python")
    make_choice(parser)


def make_choice(parser):
    args = parser.parse_args()
    if args.python_in is not None:
        generator = FileGenerator(args.python_in)
        generator.start()


if __name__ == "__main__":
    main()
