import sc2reader

TYPE_1V1 = '1v1'


def parse_replay(path):
    sc2 = sc2reader.SC2Reader()
    replay = sc2.load_replay(path)

    if replay.type != TYPE_1V1:
        raise "Unable to parse replay. Must be a 1v1 match."

    print "\nmap:"
    print replay.map_name

    print "\nstart time:"
    print replay.start_time

    players = [players[0] for players in [team.players for team in replay.teams]]
    print "players:"
    print [(p.name, p.pid) for p in players]

    if len(players) != 2:
        raise "Unable to parse replay. Must contain exactly 2 players."

    return replay

