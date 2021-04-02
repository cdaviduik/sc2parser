import sys
import time
import traceback
from replay.config import load_config
from replay.finder import find_replays
from replay.processor import process_replay, build_parsed_path

POLL_INTERVAL = 30


def find_and_parse():
    replay_config = load_config('./config.json')

    while True:
        try:
            print '\nChecking for replays'
            _execute(replay_config)
        except:
            print "\nSomething went wrong:"
            traceback.print_exc(file=sys.stdout)

        # TODO: customize poll interval
        print "\nChecking again in {} seconds".format(POLL_INTERVAL)
        time.sleep(replay_config.poll_interval)


def _execute(replay_config):
    path = replay_config.replays_path
    parsed_path = build_parsed_path(path, replay_config.parsed_replays_path)

    replay_paths = find_replays(path, parsed_path)
    for replay_path in replay_paths:
        print "\n*** Processing replay: {}".format(replay_path)


        process_replay(replay_path, parsed_path, skip_existing=replay_config.skip_existing, own_accounts=replay_config.own_accounts,
                       path_separator=replay_config.path_separator)

    print "\n*** ALL DONE ***"
    print "hopefully it worked"
