import sys


def main():
    from replay import find_and_parse

    print '\nRunning parser'
    find_and_parse()


def add_libs_to_sys_path():
    sys.path.append('./libs')


if __name__ == '__main__':
    add_libs_to_sys_path()
    main()
