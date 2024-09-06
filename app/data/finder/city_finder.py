import csv
from input_corrector import InputCorrector

class CityFinder:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.cities = self.load_cities()  # Cambié a load_cities para coincidir con el nombre del método.

    def load_cities(self):
        '''Carga todas las ciudades de la columna 'destination' en el archivo CSV.'''
        cities = []
        with open(self.csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cities.append(row['destination'])
        return cities

    def find_city(self, input_string):
        '''Encuentra la mejor coincidencia de la ciudad dada una cadena de entrada.'''
        corrector = InputCorrector()
        best_match = corrector.encuentra_coincidencia(input_string, self.cities)
        if best_match:
            return best_match.capitalize()  # Devuelve el nombre de la ciudad en formato capitalizado
        else:
            return "Ciudad no encontrada."
