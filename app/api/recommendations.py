"""
Modulo de Recomendaciones
Author: @ThePatrickCastle
Version 1.0

"""

from apiRequests import APIRequest
from jsontoCsv import JSONtoCSV 
from cityDataBaseFinder import CityDataBaseFinder as cityFinder
import csv

class Recommendations():
    '''
    Clase con métodos para crear la lista de recomendaciones que se le entregará al usuario
    
    Métodos
    ---------
    * __init__(*args)
    * complete_atributes()
    * get_atributes()
    * get_number_atributeRecommendation(file_name, atributeNo)
    * get_string_atributeRecommentation(file_name, atributeNo)
    * get_recommendations()
    
    Atributos
    ---------
    * noArgumentos (int): El numero de argumentos que recibe el constructor de clase
    * llave (str): Llave de licencia de OpenWeatherMap
    * atributes (llist): Lista donde se guardan los atributos de los objetos en Clima.csv
    * recomendaciones (list): Lista donde se guardan los strings de recomendaciones

    '''
    def __init__(self, *args):
        """
        Método constructor para las recomendaciones. Se emplea *args para simular sobrecarga de constructores.

        Args:
        nombre_Ciudad (str): Se puede inicializar el objeto solo con el nombre de la ciudad
        latitud (double): Primer argumento de coordenadas para inicializar el objeto
        longitud (double): Segundo argumento de coordenadas para inicializar el objeto
        
        """
        self.noArgumentos = len(args)
        self.llave = "310e40947f292086c33d04e2f959e7f8"
        self.atributes = []
        self.recomendaciones = []

        if len(args) == 1:
            self.nombre_Ciudad = args[0]
            
        elif len(args) == 2:
            self.latitud = args[0]
            self.longitud = args[1]
        
        self.complete_atributes();


    def complete_atributes(self):
        """
        Método que se asegura que el objeto agregue a la base de datos Clima.csv su ciudad y recupere su informacion en formato de lista

        """
        if self.noArgumentos == 1:
            if cityFinder.buscarCiudad(self.nombre_Ciudad):
               localizacion = cityFinder.getIndiceCiudad(self.nombre_Ciudad)
               self.atributes = cityFinder.getParametros(localizacion)
            else:
               nuevoJSON = APIRequest.get_formatedJSON(self.llave, 0, 0, self.nombre_Ciudad)
               JSONtoCSV.appendJSON(nuevoJSON)
               localizacion = cityFinder.getIndiceCiudad(self.nombre_Ciudad)
               self.atributes = cityFinder.getParametros(localizacion)
        else:
            if cityFinder.buscarCoordenadas(self.latitud, self.longitud):
                localizacion = cityFinder.getIndiceCoordenadas(self.latitud, self.longitud)
                self.atributes = cityFinder.getParametros(localizacion)
            else:
                nuevoJSON = APIRequest.get_formatedJSON(self.llave, self.latitud, self.longitud, "")
                JSONtoCSV.appendJSON(nuevoJSON)
                localizacion = cityFinder.getIndiceCoordenadas(self.latitud, self.longitud)
                self.atributes = cityFinder.getParametros(localizacion)

    
    def get_atributes(self):
        """
        Método que devuelve la lista de atributos de un registro en Clima.csv
        
        Returns:
        recomendaciones (list): Lista que contiene todos los elementos de la fila de un registro en Clima.csv
        
        """
        return self.atributes

      
    def get_number_atributeRecomendation(self, file_name, atributeNo):
        """
        Método que devuelve la recomendacion dada por el Csv de recomendaciones de valores numericos

        Args:
        file_name (str): Nombre del csv con las recomendaciones
        atributeNo (int): Indice del valor del atributo

        Returns:
        recommendations (str): Cadena de recomendación

        """
        target_value = float(self.atributes[atributeNo])
        csv_file = "./recomendTables/"+file_name+".csv"
        closest_weather = None
        closest_difference = float('inf')
        recommendation = None
        
        with open(csv_file, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                weather_value = float(row[file_name])
                difference = abs(weather_value - target_value)
                
                if difference < closest_difference:
                    closest_difference = difference
                    closest_weather = weather_value
                    recommendation = row['recommendation']
                    
        return recommendation

    def get_string_atributeRecomendation(self, file_name, atributeNo):
        """
        Método que devuelve la recomendacion dada por el Csv de recomendaciones de cadenas

        Args:
        file_name (str): Nombre del csv con las recomendaciones
        atributeNo (int): Indice del valor del atributo

        Returns:
        recommendations (str): Cadena de recomendación

        """
        target_value = self.atributes[atributeNo]
        csv_file = "./recomendTables/"+file_name+".csv"
    
        with open(csv_file, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                weather_value = row[file_name]
                
                if weather_value == target_value:
                    recommendation = row['recommendation']
                    
        return recommendation


                
    def get_recommendations(self):
        """
        Método que devuelve el arreglo de recomendaciones por campo de interés.

        Args:
        file_name (str): Nombre del csv con las recomendaciones
        atributeNo (int): Indice del valor del atributo
        
        Returns:
        recomendaciones (list): Lista con todas las recomendaciones 

        """
        weather_main = self.get_string_atributeRecomendation("weather_main", 4)
        temp = self.get_number_atributeRecomendation("temp", 5)
        feels_like = self.get_number_atributeRecomendation("feels_like", 6)
        humidity = self.get_number_atributeRecomendation("humidity", 7)
        wind_speed = self.get_number_atributeRecomendation("wind_speed", 8)

        if temp == feels_like:
            self.recomendaciones = [weather_main, temp, humidity, wind_speed]
        else:
            self.recomendaciones = [weather_main, temp, feels_like, humidity, wind_speed]
        
        return self.recomendaciones
        


        

    
    
    
