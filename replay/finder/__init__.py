import glob

from replay.common import REPLAY_EXT


class ReplayFinderError(Exception):
    pass


def find_replays(path):
    search_path = '{}/*.{}'.format(path, REPLAY_EXT)

    print "\nfiles in glob:"
    replay_paths = glob.glob(search_path)
    print replay_paths

    if len(replay_paths) == 0:
        raise ReplayFinderError('Unable to find any replays in path {}'.format(search_path))

    return replay_paths

