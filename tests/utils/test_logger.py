import os
import unittest
from io import StringIO
from logging import StreamHandler

from src.utils.logger import get_logger, setup_logging


class TestLoggingSetup(unittest.TestCase):

    def setUp(self):
        # Ensure we start with a clean slate
        self.log_dir = "logs"
        self.log_file = "app.log"
        self.log_file_path = os.path.join(self.log_dir, self.log_file)

        if os.path.exists(self.log_dir):
            for f in os.listdir(self.log_dir):
                os.remove(os.path.join(self.log_dir, f))
            os.rmdir(self.log_dir)

        # Setup the logging configuration
        setup_logging()

    def tearDown(self):
        # Cleanup after tests
        if os.path.exists(self.log_dir):
            for f in os.listdir(self.log_dir):
                os.remove(os.path.join(self.log_dir, f))
            os.rmdir(self.log_dir)

    def test_log_directory_creation(self):
        self.assertTrue(os.path.exists(self.log_dir), "Log directory was not created")

    def test_log_file_creation(self):
        self.assertTrue(os.path.exists(self.log_file_path), "Log file was not created")

    def test_log_output(self):
        logger = get_logger(__name__)
        log_message = "This is a test message."

        # Capture log output
        with StringIO() as log_output:
            # Add a stream handler to capture console output
            console_handler = StreamHandler(log_output)
            logger.addHandler(console_handler)

            # Log a message
            logger.info(log_message)

            # Get log output and check if message is present
            log_output.seek(0)
            log_output_content = log_output.getvalue()
            self.assertIn(
                log_message,
                log_output_content,
                "Log message was not found in the console output",
            )

        # Verify that the message is in the log file
        with open(self.log_file_path, "r") as log_file:
            log_file_content = log_file.read()
            self.assertIn(
                log_message,
                log_file_content,
                "Log message was not found in the log file",
            )


if __name__ == "__main__":
    unittest.main()
