import pandas as pd


class DataProcessor:
    @staticmethod
    def format_theses_data(data: pd.DataFrame) -> pd.DataFrame:

        # Create dynamic columns for topics based on the language used
        data['subjects'] = data['subjects'].apply(lambda x: x if isinstance(x, list) else [])
        languages = set(lang['langue'] for subjects in data['subjects'] for lang in subjects)
        for lang in languages:
            data[f'topic_{lang}'] = data['subjects'].apply(lambda subjects: ', '.join(
                item['libelle'] for item in subjects if item['langue'] == lang
            ))

        data = data.drop(columns=['subjects'])

        # Convert all string columns to lowercase, trimming whitespace
        str_columns = data.select_dtypes(include=['object']).columns
        for col in str_columns:
            if data[col].dtype == 'object':
                data[col] = data[col].str.lower().str.strip()

        # Drop duplicates, fill NaN values, convert string column to datetime
        data = data.drop_duplicates().reset_index(drop=True)
        data = data.fillna('')
        data['date_submission'] = pd.to_datetime(data['date_submission'], errors='coerce')

        return data
