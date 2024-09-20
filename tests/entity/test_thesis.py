import pytest

from src.entity.thesis import Thesis


def test_thesis_initialization():
    thesis = Thesis(
        discipline="Computer Science",
        status="Soutenu",
        title_fr="Titre en Français",
        title_en="Title in English",
        subjects=["AI", "Machine Learning"],
        date_submission="2023-01-15",
    )
    assert thesis.discipline == "Computer Science"
    assert thesis.status == "Soutenu"
    assert thesis.title_fr == "Titre en Français"
    assert thesis.title_en == "Title in English"
    assert thesis.date_submission == "2023-01-15"


# noinspection PyTypeChecker
def test_thesis_invalid_date():
    with pytest.raises(ValueError):
        Thesis(
            discipline="CS",
            status="Soutenu",
            title_fr="Fr",
            title_en="En",
            subjects=["AI"],
            date_submission=2023,  # Invalid type for date_submission
        )
