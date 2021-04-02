import os
import glob

from replay.common import REPLAY_EXT, DEFAULT_PARSED_PATH_NAME
from replay.common.logger import log


class ReplayFinderError(Exception):
    pass


def find_replays(path, parsed_path):
    print "\nsearching for replays in path"
    for dir_path, dir_names, file_names in os.walk(path):
        log('dir path', dir_path)

        if _should_skip_path(dir_path, parsed_path):
            print "Skipping parsed directory"
            continue
        for filename in glob.iglob(_search_path(dir_path)):
            yield filename


def _search_path(path):
    return '{}/*.{}'.format(path, REPLAY_EXT)


def _should_skip_path(path, parsed_path):
    return path.endswith(DEFAULT_PARSED_PATH_NAME) or path.endswith(parsed_path)
