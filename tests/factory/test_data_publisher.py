import os
import pandas as pd
from unittest.mock import patch
from src.factory.data_publisher import DataPublisher


@patch('os.makedirs')
@patch('pandas.DataFrame.to_csv')
def test_upload_dataset(mock_to_csv, mock_makedirs):
    # Sample DataFrame to be saved
    sample_data = pd.DataFrame({
        'title_fr': ['Thèse 1', 'Thèse 2'],
        'year': [2022, 2023]
    })

    # Call the method with a sample DataFrame and a dataset name
    dataset_name = 'french_theses_dataset'
    DataPublisher.upload_dataset(sample_data, dataset_name)

    # Assert os.makedirs was called to create the dataset directory
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    dataset_folder = os.path.join(root_dir, 'dataset')
    mock_makedirs.assert_called_once_with(dataset_folder, exist_ok=True)

    # Assert DataFrame.to_csv was called with the correct file path
    expected_csv_path = os.path.join(dataset_folder, f'{dataset_name}.csv')
    mock_to_csv.assert_called_once_with(expected_csv_path, index=False)
