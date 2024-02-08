from gendiff.utils import parse_args
from gendiff import generate_diff


def main():
    args = parse_args()
    print(generate_diff(args.firstfile, args.secondfile))


if __name__ == '__main__':
    main()
