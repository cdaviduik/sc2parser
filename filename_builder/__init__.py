REPLAY_EXT = 'SC2Replay'


def build_filename(start_time, map_name, players):
    filename_data = {
        'start_time': start_time,
        'map_name': map_name,
        'ext': REPLAY_EXT,
        'player1_info': build_player_info(players[0]),
        'player2_info': build_player_info(players[1]),
    }
    return '{start_time} {map_name} {player1_info} {player2_info}.{ext}'.format(**filename_data)


def build_player_info(player):
    return '{} {}'.format(player.name, player.mmr)