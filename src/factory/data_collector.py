import requests
import pandas as pd
from typing import List, Dict, Any
from dataclasses import asdict
from entity.thesis import Thesis
from utils.config import config


class DataCollector:
    def __init__(self):
        self.api_url = config.get('API.FR_THESES_URL')
        if not self.api_url:
            raise ValueError("API URL not configured properly.")

    def fetch_theses(self, query: str = '*', start: int = 0, size: int = 100, sort: str = 'dateDesc') -> pd.DataFrame:

        all_theses = []

        while True:
            params = {
                'q': query,
                'debut': start,
                'nombre': size,
                'tri': sort
            }
            response = requests.get(self.api_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            theses = self._parse_theses(data)
            if not theses:
                break
            all_theses.extend(theses)
            start += size  # Move to the next page

        # Convert list of Thesis objects to DataFrame
        df = pd.DataFrame([asdict(thesis) for thesis in all_theses])
        return df

    @staticmethod
    def _parse_theses(data: Dict[str, Any]) -> List[Thesis]:
        theses = []
        for item in data.get('theses', []):
            title_fr = item.get('titrePrincipal')
            title_en = item.get('titreEN')

            if title_fr or title_en:  # Include if it has a summary in either language
                thesis = Thesis(
                    discipline=item.get('discipline', ''),
                    status=item.get('status', ''),
                    title_fr=title_fr,
                    title_en=title_en,
                    subjects=item.get('sujets', []),
                    date_submission=item.get('dateSoutenance', '')
                )
                theses.append(thesis)
        return theses
