import unittest
from GettingStarted.city_functions import city_formatter

class TestCityFunctions(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        formatted = city_formatter('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')

    def test_city_country_pop(self):
        formatted = city_formatter('santiago', 'chile', 5000000)
        self.assertEqual(formatted, 'Santiago, Chile - Population 5000000')



unittest.main()