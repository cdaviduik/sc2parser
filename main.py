import sys
import time


def main():
    from replay import find_and_parse

    print '\nRunning parser'
    while True:
        print '\nChecking for replays'
        find_and_parse()

        # time.sleep(1)
        return


def add_libs_to_sys_path():
    sys.path.append('./libs')


if __name__ == '__main__':
    add_libs_to_sys_path()
    main()
