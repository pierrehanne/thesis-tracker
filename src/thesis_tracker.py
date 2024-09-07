from factory.data_collector import DataCollector
from factory.data_processor import DataProcessor
from factory.data_publisher import DataPublisher
from utils.logger import setup_logging, get_logger  # Import logging functions


def main():
    # Setup logging
    setup_logging()  # Initialize logging (log to file and console)
    logger = get_logger(__name__)  # Create a logger instance

    # Log the start of the process
    logger.info("Starting thesis tracking process")

    try:
        # Instantiate Factory Decorators
        logger.info("Initializing DataCollector, DataProcessor, and DataPublisher")
        collector = DataCollector()
        processor = DataProcessor()
        publisher = DataPublisher()

        # Apply Factory Decorators
        logger.info("Fetching thesis data")
        df = collector.fetch_theses()

        logger.info("Processing thesis data")
        formatted_df = processor.format_theses_data(df)

        logger.info("Publishing dataset")
        publisher.upload_dataset(formatted_df)

        logger.info("Thesis tracking process completed successfully")

    except Exception as e:
        # Log any errors that occur during the process
        logger.error(f"An error occurred during the thesis tracking process: {e}", exc_info=True)


if __name__ == "__main__":
    main()
