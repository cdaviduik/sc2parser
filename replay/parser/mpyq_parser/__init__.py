import mpyq
import json


def parse_replay(path):
    archive = mpyq.MPQArchive(path)
    # archive.extract_to_disk()
    jsondata = archive.read_file("replay.gamemetadata.json").decode("utf-8")
    obj = json.loads(jsondata)

    print "\nobj:"
    print obj

    return obj


def find_player_mmr_with_id(players, pid):
    for p in players:
        if p.get('PlayerID') == pid:
            return p.get('MMR')

    return None
