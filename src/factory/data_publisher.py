import os
import pandas as pd


class DataPublisher:

    @staticmethod
    def upload_dataset(dataframe: pd.DataFrame, dataset_name: str = 'french_theses_dataset'):

        # Define the path to the dataset folder in the root of the project
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        dataset_folder = os.path.join(root_dir, 'dataset')

        # Ensure the dataset folder exists
        os.makedirs(dataset_folder, exist_ok=True)

        # List of unique years in the dataset
        dataframe.to_csv(os.path.join(dataset_folder, f'{dataset_name}.csv'), index=False)