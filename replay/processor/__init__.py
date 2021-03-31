from replay.file_io import copy_file
from replay.parser import parse_replay
from replay.filename_builder import build_filename


def process_replay(path, skip_existing=True, own_accounts=None):
    replay = parse_replay(path)

    new_filename = build_filename(replay.start_time, replay.map_name, replay.players,
                                  own_accounts=own_accounts)

    print "\nnew_filename:"
    print new_filename

    copy_file(path, new_filename, skip_existing)
