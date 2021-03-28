import os
import sys

sys.path.append('./libs')

from file_io import copy_file
from parser import parse_replay
from filename_builder import build_filename


REPLAY_EXT = 'SC2Replay'


def main():
    path = get_path()

    replay = parse_replay(path)

    new_filename = build_filename(replay.start_time, replay.map_name, replay.players)

    print "\nnew_filename:"
    print new_filename

    copy_file(path, new_filename)

    print "\n*** ALL DONE ***"
    print "hopefully it worked"


def get_path():
    path = sys.argv[1]
    fullpath = os.path.abspath(path)
    print "\nfullpath:", fullpath
    return fullpath


if __name__ == '__main__':
    main()
