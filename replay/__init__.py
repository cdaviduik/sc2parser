from replay.config import load_config
from replay.finder import find_replays
from replay.processor import process_replay


def find_and_parse():
    replay_config = load_config('./config.json')
    path = replay_config.replays_path

    replay_paths = find_replays(path)
    for replay_path in replay_paths:
        process_replay(replay_path, skip_existing=replay_config.skip_existing, own_accounts=replay_config.own_accounts)

    print "\n*** ALL DONE ***"
    print "hopefully it worked"
