from factory.data_collector import DataCollector
from factory.data_processor import DataProcessor
from factory.data_publisher import DataPublisher


def main():

    # Instantiate Factory Decorators
    collector = DataCollector()
    processor = DataProcessor()
    publisher = DataPublisher()

    # Apply Factory Decorators
    df = collector.fetch_theses()
    formatted_df = processor.format_theses_data(df)
    publisher.upload_dataset(formatted_df)


if __name__ == "__main__":
    main()
