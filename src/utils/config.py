import yaml
import os


class Config:
    def __init__(self, config_file='config.yaml'):
        if not os.path.isfile(config_file):
            raise FileNotFoundError(f"Configuration file '{config_file}' not found.")

        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)

        # Debug: Print the loaded configuration
        print("Loaded configuration:", self.config)

    def get(self, key, default=None):
        # Split the key into nested levels
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, default)
            if value == default:
                return default
        # Expand environment variables in string values
        if isinstance(value, str):
            value = os.path.expandvars(value)
        return value


# Create an instance of Config
config = Config()
