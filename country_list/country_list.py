import csv
from functools import lru_cache
from operator import itemgetter
from pathlib import Path

data_dir = Path(__file__).parent / "country_data" / "data"


@lru_cache(1)
def available_languages():
    return sorted(x.name for x in data_dir.iterdir() if (x / "country.csv").exists())


@lru_cache()
def countries_for_language(lang):
    path = data_dir / _clean_lang(lang) / "country.csv"
    with path.open() as file_:
        return list(map(itemgetter("id", "value"), csv.DictReader(file_)))


def _clean_lang(lang):
    cleaned_lang = lang.replace("-", "_").lower()
    try:
        return _languages()[cleaned_lang]
    except KeyError:
        raise ValueError("Language {} not found".format(lang)) from None


@lru_cache(1)
def _languages():
    return {language.lower(): language for language in available_languages()}
