import unittest
from unittest.mock import mock_open, patch

from src.utils.config import Config


class TestConfig(unittest.TestCase):

    @patch("os.path.isfile")
    @patch("builtins.open", new_callable=mock_open, read_data="key: value")
    @patch("yaml.safe_load")
    def test_config_initialization(
        self, mock_yaml_safe_load, mock_open_file, mock_isfile
    ):
        # Mock that the config file exists
        mock_isfile.return_value = True

        # Mock YAML loading to return a dict
        mock_yaml_safe_load.return_value = {
            "key": "value",
            "nested": {"subkey": "subvalue"},
        }

        # Test the Config constructor and get method
        config = Config("config.yaml")

        # Verify YAML load was called
        mock_open_file.assert_called_once_with("config.yaml", "r")
        mock_yaml_safe_load.assert_called_once()

        # Test fetching values from config
        self.assertEqual(config.get("key"), "value")
        self.assertEqual(config.get("nested.subkey"), "subvalue")

    @patch("os.path.isfile")
    def test_missing_config_file(self, mock_isfile):
        # Mock the case where the config file doesn't exist
        mock_isfile.return_value = False

        # Check if FileNotFoundError is raised
        with self.assertRaises(FileNotFoundError):
            Config("nonexistent.yaml")

    @patch("os.path.isfile")
    @patch("builtins.open", new_callable=mock_open, read_data="key: $ENV_VAR")
    @patch("yaml.safe_load")
    @patch("os.path.expandvars")
    def test_environment_variable_expansion(
        self, mock_expandvars, mock_yaml_safe_load, mock_open_file, mock_isfile
    ):
        # Mock file existence and YAML loading
        mock_isfile.return_value = True
        mock_yaml_safe_load.return_value = {"key": "$ENV_VAR"}

        # Mock environment variable expansion
        mock_expandvars.side_effect = lambda x: x.replace("$ENV_VAR", "expanded_value")

        config = Config("config.yaml")

        # Test if environment variable is expanded
        self.assertEqual(config.get("key"), "expanded_value")

    @patch("os.path.isfile")
    @patch("builtins.open", new_callable=mock_open, read_data="key: value")
    @patch("yaml.safe_load")
    def test_missing_key_with_default(
        self, mock_yaml_safe_load, mock_open_file, mock_isfile
    ):
        # Mock file existence and YAML loading
        mock_isfile.return_value = True
        mock_yaml_safe_load.return_value = {"key": "value"}

        config = Config("config.yaml")

        # Test key not found and default value returned
        self.assertEqual(
            config.get("nonexistent", default="default_value"), "default_value"
        )

    @patch("os.path.isfile")
    @patch("builtins.open", new_callable=mock_open, read_data="key: value")
    @patch("yaml.safe_load")
    def test_partial_key_access(self, mock_yaml_safe_load, mock_open_file, mock_isfile):
        # Mock file existence and YAML loading
        mock_isfile.return_value = True
        mock_yaml_safe_load.return_value = {"key": {"subkey": "value"}}

        config = Config("config.yaml")

        # Test partial key access
        self.assertEqual(config.get("key.subkey"), "value")
        self.assertEqual(
            config.get("key.nonexistent", default="default_value"), "default_value"
        )


if __name__ == "__main__":
    unittest.main()
