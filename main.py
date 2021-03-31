import sys

from replay import find_and_parse


def main():
    find_and_parse()


def add_libs_to_sys_path():
    sys.path.append('./libs')


if __name__ == '__main__':
    add_libs_to_sys_path()
    main()
