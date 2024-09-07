import logging
import os

# Define log file location and format
LOG_DIR = 'logs'
LOG_FILE = 'app.log'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def setup_logging(level: int = logging.INFO) -> None:
    # Create log directory if it doesn't exist
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # Define the full path for the log file
    log_file_path = os.path.join(LOG_DIR, LOG_FILE)

    # Create a logger object
    logger = logging.getLogger()
    logger.setLevel(level)

    # Create handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_file_path)

    # Set the logging format for handlers
    formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Remove any existing handlers to prevent duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
