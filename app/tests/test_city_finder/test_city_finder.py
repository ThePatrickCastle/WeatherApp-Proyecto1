import unittest
from app.data.finder.city_finder import CityFinder

class TestCityFinder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Este método se ejecuta una vez antes de todas las pruebas.
        cls.city_finder = CityFinder('app/data/finder/dataset1.csv')

    def test_find_city_exact_match(self):
        # Prueba con una entrada exacta
        self.assertEqual(self.city_finder.find_city('Monterrey'), 'Monterrey')

    def test_find_city_fuzzy_match(self):
        # Prueba con una entrada cercana
        self.assertEqual(self.city_finder.find_city('montery'), 'Monterrey')

    def test_find_city_not_found(self):
        # Prueba cuando no se encuentra ninguna ciudad
        self.assertEqual(self.city_finder.find_city('NonExistentCity'), 'Ciudad no encontrada.')

if __name__ == '__main__':
    unittest.main()
