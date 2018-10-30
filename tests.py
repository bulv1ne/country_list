import unittest

import country_list


class TestCountryList(unittest.TestCase):
    def test_available_languages(self):
        self.assertEqual(
            len(country_list.available_languages()),
            586,
            "Languages have been added/removed",
        )

    def test_countries(self):
        self.assertEqual(
            len(country_list.countries_for_language("sv_SE")),
            255,
            "Countries have been added/removed",
        )

    def test_invalid_country(self):
        with self.assertRaises(ValueError):
            country_list.countries_for_language("invalid")

    def test_auto_format_language(self):
        self.assertEqual(
            country_list.countries_for_language("sv_SE"),
            country_list.countries_for_language("sv-se"),
        )
