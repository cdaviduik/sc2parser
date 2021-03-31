from replay.parser.mpyq_parser import parse_replay as parse_replay_mpyq, find_player_mmr_with_id
from replay.parser.sc2reader_parser import parse_replay as parse_replay_sc2reader


def parse_replay(path):
    replay = Replay(path)
    replay.parse()
    return replay


class Replay:
    def __init__(self, path):
        self.path = path
        self._mpyq_replay = None
        self._sc2reader_replay = None

    def parse(self):
        self._mpyq_replay = parse_replay_mpyq(self.path)
        self._sc2reader_replay = parse_replay_sc2reader(self.path)

    @property
    def start_time(self):
        return self._sc2reader_replay.start_time

    @property
    def map_name(self):
        return self._sc2reader_replay.map_name

    @property
    def players(self):
        players = []

        mpyq_players = self._mpyq_replay['Players']
        sc2reader_players = [team_players[0] for team_players in [team.players for team in self._sc2reader_replay.teams]]

        for p in sc2reader_players:
            mmr = find_player_mmr_with_id(mpyq_players, p.pid)
            players.append(Player(p, mmr))

        return players


class Player:
    def __init__(self, player, mmr):
        self._player = player
        self.mmr = mmr

    @property
    def name(self):
        return self._player.name


# Example of parsed mpyq data
data = {u'GameVersion': u'5.0.6.83830', u'DataVersion': u'B4745D6A4F982A3143C183D8ACB6C3E3', u'BaseBuild': u'Base83830',
        u'Title': u'Deathaura LE', u'DataBuild': u'83830', u'Players': [
        {u'AssignedRace': u'Zerg', u'PlayerID': 1, u'MMR': 2852, u'SelectedRace': u'Zerg', u'Result': u'Win',
         u'APM': 139.0},
        {u'AssignedRace': u'Prot', u'PlayerID': 2, u'MMR': 2834, u'SelectedRace': u'Prot', u'Result': u'Loss',
         u'APM': 148.0}], u'Duration': 1321}

data2 = {u'GameVersion': u'5.0.6.83830', u'DataVersion': u'B4745D6A4F982A3143C183D8ACB6C3E3', u'BaseBuild': u'Base83830',
        u'Title': u'Lightshade LE', u'DataBuild': u'83830', u'Players': [
        {u'AssignedRace': u'Terr', u'PlayerID': 1, u'MMR': 3314, u'SelectedRace': u'Terr', u'Result': u'Loss',
         u'APM': 167.0},
        {u'AssignedRace': u'Zerg', u'PlayerID': 2, u'MMR': 3423, u'SelectedRace': u'Zerg', u'Result': u'Win',
         u'APM': 160.0}], u'Duration': 550}

