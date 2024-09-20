import unittest
from unittest.mock import MagicMock, patch

from src.thesis_tracker import main


class TestThesisTracker(unittest.TestCase):

    @patch("src.thesis_tracker.setup_logging")
    @patch("src.thesis_tracker.get_logger")
    @patch("src.thesis_tracker.DataPublisher")
    @patch("src.thesis_tracker.DataProcessor")
    @patch("src.thesis_tracker.DataCollector")
    def test_main_success(
        self,
        mock_data_collector,
        mock_data_processor,
        mock_data_publisher,
        mock_get_logger,
        mock_setup_logging,
    ):
        # Mock logging setup and logger instance
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger

        # Mock the DataCollector, DataProcessor, and DataPublisher instances
        mock_collector_instance = mock_data_collector.return_value
        mock_processor_instance = mock_data_processor.return_value
        mock_publisher_instance = mock_data_publisher.return_value

        # Mock DataCollector.fetch_theses
        mocked_fetch_theses_df = MagicMock()
        mock_collector_instance.fetch_theses.return_value = mocked_fetch_theses_df

        # Mock DataProcessor.format_theses_data
        mocked_formatted_df = MagicMock()
        mock_processor_instance.format_theses_data.return_value = mocked_formatted_df

        # Run the main function
        main()

        # Assert that setup_logging was called once
        mock_setup_logging.assert_called_once()

        # Assert that get_logger was called with the correct name
        # Adjusted to match the actual module name during testing
        mock_get_logger.assert_called_once_with("src.thesis_tracker")

        # Assert logging statements
        expected_info_calls = [
            unittest.mock.call("Starting thesis tracking process"),
            unittest.mock.call(
                "Initializing DataCollector, DataProcessor, and DataPublisher"
            ),
            unittest.mock.call("Fetching thesis data"),
            unittest.mock.call("Processing thesis data"),
            unittest.mock.call("Publishing dataset"),
            unittest.mock.call("Thesis tracking process completed successfully"),
        ]
        mock_logger.info.assert_has_calls(expected_info_calls, any_order=False)

        # Assert that fetch_theses was called once
        mock_collector_instance.fetch_theses.assert_called_once()

        # Assert that format_theses_data was called once
        mock_processor_instance.format_theses_data.assert_called_once_with(
            mocked_fetch_theses_df
        )

        # Assert that upload_dataset was called
        mock_publisher_instance.upload_dataset.assert_called_once_with(
            mocked_formatted_df
        )

    @patch("src.thesis_tracker.setup_logging")
    @patch("src.thesis_tracker.get_logger")
    @patch("src.thesis_tracker.DataPublisher")
    @patch("src.thesis_tracker.DataProcessor")
    @patch("src.thesis_tracker.DataCollector")
    def test_main_with_exception(
        self,
        mock_data_collector,
        mock_data_processor,
        mock_data_publisher,
        mock_get_logger,
        mock_setup_logging,
    ):
        # Mock logging setup and logger instance
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger

        # Mock the DataCollector, DataProcessor, and DataPublisher instances
        mock_collector_instance = mock_data_collector.return_value
        mock_processor_instance = mock_data_processor.return_value
        mock_publisher_instance = mock_data_publisher.return_value

        # Simulate DataCollector.fetch_theses raising an exception
        mock_collector_instance.fetch_theses.side_effect = Exception("API failure")

        # Run the main function
        main()

        # Assert that setup_logging was called once
        mock_setup_logging.assert_called_once()

        # Assert that get_logger was called with the correct name
        mock_get_logger.assert_called_once_with("src.thesis_tracker")

        # Assert that starting and initializing logs were called
        expected_info_calls = [
            unittest.mock.call("Starting thesis tracking process"),
            unittest.mock.call(
                "Initializing DataCollector, DataProcessor, and DataPublisher"
            ),
            unittest.mock.call("Fetching thesis data"),
        ]
        mock_logger.info.assert_has_calls(expected_info_calls, any_order=False)

        # Assert that an error was logged
        mock_logger.error.assert_called_once()
        error_call_args = mock_logger.error.call_args
        self.assertIn(
            "An error occurred during the thesis tracking process: API failure",
            error_call_args[0][0],
        )

        # Assert that methods were not called due to the exception
        mock_processor_instance.format_theses_data.assert_not_called()
        mock_publisher_instance.upload_dataset.assert_not_called()


if __name__ == "__main__":
    unittest.main()
