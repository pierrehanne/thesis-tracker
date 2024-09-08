import os

import yaml


class Config:
    def __init__(self, config_file='config.yaml'):

        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        config_file_path = os.path.join(base_dir, config_file)

        if not os.path.isfile(config_file_path):
            raise FileNotFoundError(f"Configuration file '{config_file_path}' not found.")

        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)

    def get(self, key, default=None):

        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, default)
            if value == default:
                return default

        if isinstance(value, str):
            value = os.path.expandvars(value)
        return value


config = Config()
