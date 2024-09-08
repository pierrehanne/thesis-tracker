import pytest
import pandas as pd
from src.factory.data_processor import DataProcessor


def test_format_theses_data():
    # Create a test DataFrame with the additional fields from the API response
    data = pd.DataFrame({
        'subjects': [
            [{'langue': 'fr', 'libelle': 'Responsabilité'}, {'langue': 'en', 'libelle': 'Responsibility'}],
            [{'langue': 'fr', 'libelle': 'Science'}, {'langue': 'en', 'libelle': 'Science'}]
        ],
        'title_fr': ['Titre en français', 'Titre scientifique'],
        'title_en': ['French title', 'Scientific title'],
        'discipline': ['droit', 'sciences'],
        'status': ['soutenue', 'en préparation'],
        'date_submission': ['2023-01-15', '2023-05-20']
    })

    # Instantiate the DataProcessor and format the data
    processor = DataProcessor()
    formatted_data = processor.format_theses_data(data)

    # Test that the dynamic language-based columns are created
    assert 'topic_fr' in formatted_data.columns
    assert 'topic_en' in formatted_data.columns

    # Test that the subjects were properly formatted and converted to lowercase
    assert formatted_data['topic_fr'].iloc[0] == 'responsabilité'
    assert formatted_data['topic_en'].iloc[0] == 'responsibility'
    assert formatted_data['topic_fr'].iloc[1] == 'science'
    assert formatted_data['topic_en'].iloc[1] == 'science'

    # Test that other string columns are converted to lowercase and trimmed
    assert formatted_data['title_fr'].iloc[0] == 'titre en français'
    assert formatted_data['title_en'].iloc[0] == 'french title'
    assert formatted_data['discipline'].iloc[0] == 'droit'
    assert formatted_data['status'].iloc[1] == 'en préparation'

    # Test that date_submission was converted to datetime format
    assert pd.api.types.is_datetime64_any_dtype(formatted_data['date_submission'])

    # Ensure duplicates are removed and NaN values are filled (not directly applicable in this test)
    assert formatted_data.isnull().sum().sum() == 0  # No NaN values
    assert len(formatted_data) == 2  # No rows dropped
