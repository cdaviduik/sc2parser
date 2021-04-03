import sys
import time
import traceback

from replay.cache import load_cache, write_cache
from replay.common.logger import log
from replay.config import load_config
from replay.finder import find_replays
from replay.processor import process_replay, build_parsed_path


def find_and_parse():
    replay_config = load_config('./config.json')
    initial_cache = load_cache(replay_config.parsed_replays_path,
                               enable_caching=replay_config.enable_caching) if replay_config.skip_existing else []

    while True:
        try:
            print '\nChecking for replays'
            new_parsed_cache = _execute(replay_config, initial_cache)
            write_cache(new_parsed_cache, replay_config.parsed_replays_path,
                        enable_caching=replay_config.enable_caching)
            initial_cache = new_parsed_cache
        except:
            print "\nSomething went wrong:"
            traceback.print_exc(file=sys.stdout)

        print "\nChecking again in {} seconds".format(replay_config.poll_interval)
        time.sleep(replay_config.poll_interval)


def _execute(replay_config, initial_cache):
    path = replay_config.replays_path
    parsed_path = build_parsed_path(path, replay_config.parsed_replays_path)
    parsed_cache = initial_cache

    replay_paths = find_replays(path, parsed_path)
    for replay_path in replay_paths:
        if replay_path in parsed_cache:
            log('skipping cached file', replay_path)
            continue

        print "\n*** Processing replay: {}".format(replay_path)
        process_replay(path, replay_path, parsed_path, skip_existing=replay_config.skip_existing, own_accounts=replay_config.own_accounts,
                       path_separator=replay_config.path_separator)
        parsed_cache.append(replay_path)

    print "\n*** ALL DONE ***"
    print "hopefully it worked"

    return parsed_cache
