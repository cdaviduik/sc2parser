import time
import datetime
import unicodedata

from replay.common import REPLAY_EXT
from replay.common.logger import log


def build_filename(start_time, map_name, players, own_accounts=None):
    player_infos = filter(None, [build_player_info(player, own_accounts=own_accounts) for player in players])
    log('player infos', player_infos)

    formatted_start_time = time.mktime(start_time.timetuple())

    filename_data = {
        'start_time': formatted_start_time,
        'map_name': map_name,
        'ext': REPLAY_EXT,
        'player_infos': ' '.join(player_infos)
    }
    return '{start_time} {map_name} {player_infos}.{ext}'.format(**filename_data)


def build_player_info(player, own_accounts=None):
    own_accounts = own_accounts or []
    log('own_accounts', own_accounts)
    player_name = unicodedata.normalize('NFKD', player.name).encode('ascii', 'ignore')

    if player_name in own_accounts:
        log('own player', player_name)
        return player_name

    return '{} {}'.format(player_name, player.mmr)