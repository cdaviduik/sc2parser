import json


class Config:
    def __init__(self, config_data):
        self._config_data = config_data

    def _get_config(self, key):
        return self._config_data[key]

    @property
    def replays_path(self):
        return self._get_config('replays_path')

    @property
    def skip_existing(self):
        return self._get_config('skip_existing')

    @property
    def own_accounts(self):
        return self._get_config('own_accounts')


def load_config(config_path):
    with open(config_path) as config_json:
        config_data = json.load(config_json)
        print "\nFound config:"
        print config_data
        return Config(config_data)

