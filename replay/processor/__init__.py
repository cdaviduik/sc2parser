import sys
import traceback

from replay.common import DEFAULT_PARSED_PATH_NAME
from replay.file_io import copy_file
from replay.parser import parse_replay
from replay.parser.sc2reader_parser import SC2ReaderParsingError
from replay.filename_builder import build_filename


def process_replay(path, parsed_path, skip_existing=True, own_accounts=None, path_separator=None):
    try:
        replay = parse_replay(path)
    # TODO: replace with base ParsingError
    except SC2ReaderParsingError as e:
        print "\nUnable to parse replay:"
        print e.message
        print "Skipping replay"
        return
    except:
        print "\nSomething went wrong:"
        traceback.print_exc(file=sys.stdout)
        print "Skipping replay"
        return

    new_filename = build_filename(replay.start_time, replay.map_name, replay.players,
                                  own_accounts=own_accounts)

    print "\nnew_filename:"
    print new_filename

    copy_file(path, new_filename, parsed_path, skip_existing=skip_existing, path_separator=path_separator)


def build_parsed_path(replays_path, parsed_path=None):
    if parsed_path:
        return parsed_path

    return '{}/{}'.format(replays_path, DEFAULT_PARSED_PATH_NAME)