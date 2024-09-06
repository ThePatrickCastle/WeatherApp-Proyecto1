import csv
from inputCorrector import InputCorrector

class CityFinder:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.cities = self.load_cities()

    def carga_ciudades(self):
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
            return "City not found."

# Uso del programa
city_finder = CityFinder('dataset1.csv')

# Ejemplo de búsqueda de una ciudad
input_string = "montery"  # Reemplaza con la cadena que deseas buscar
print(city_finder.find_city(input_string))
    
    
