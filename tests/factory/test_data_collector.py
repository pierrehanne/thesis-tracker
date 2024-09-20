import unittest
from unittest.mock import patch

from src.factory.data_collector import DataCollector


class TestDataCollector(unittest.TestCase):

    @patch("src.factory.data_collector.config.get")
    def test_init_with_valid_api_url(self, mock_config_get):
        # Mock config.get to return a valid API URL
        mock_config_get.return_value = "https://api.example.com/theses"

        collector = DataCollector()
        self.assertEqual(collector.api_url, "https://api.example.com/theses")

    @patch("src.factory.data_collector.config.get")
    def test_init_with_invalid_api_url(self, mock_config_get):
        # Mock config.get to return None or empty string
        mock_config_get.return_value = None

        # Check if ValueError is raised when no API URL is configured
        with self.assertRaises(ValueError):
            DataCollector()


if __name__ == "__main__":
    unittest.main()
