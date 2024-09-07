from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Thesis:
    discipline: str
    status: str
    title_fr: str
    title_en: str
    subjects: List[str]
    date_submission: Optional[str] = None

    def __post_init__(self):
        if self.date_submission and not isinstance(self.date_submission, str):
            raise ValueError("date_submission must be a string if provided.")
