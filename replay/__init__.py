import sys
import time
import traceback
from replay.config import load_config
from replay.finder import find_replays
from replay.processor import process_replay


POLL_INTERVAL = 30


def find_and_parse():
    while True:
        try:
            print '\nChecking for replays'
            _execute()
        except:
            print "\nSomething went wrong:"
            traceback.print_exc(file=sys.stdout)

        # TODO: customize poll interval
        print "\nChecking again in {} seconds".format(POLL_INTERVAL)
        time.sleep(POLL_INTERVAL)


def _execute():
    replay_config = load_config('./config.json')
    path = replay_config.replays_path

    replay_paths = find_replays(path)
    for replay_path in replay_paths:
        print "\n*** Processing replay: {}".format(replay_path)
        process_replay(replay_path, skip_existing=replay_config.skip_existing, own_accounts=replay_config.own_accounts)

    print "\n*** ALL DONE ***"
    print "hopefully it worked"