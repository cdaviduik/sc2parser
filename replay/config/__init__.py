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

    @property
    def poll_interval(self):
        return self._get_config('poll_interval')

    @property
    def path_separator(self):
        return self._get_config('path_separator')

    @property
    def parsed_replays_path(self):
        return self._get_config('parsed_replays_path')

    @property
    def enable_caching(self):
        return self._get_config('enable_caching')


def load_config(config_path):
    with open(config_path) as config_json:
        config_data = json.load(config_json)
        print "\nFound config:"
        print config_data
        return Config(config_data)

