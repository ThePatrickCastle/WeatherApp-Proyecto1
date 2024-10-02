"""
Modulo de Recomendaciones
Author: @ThePatrickCastle
Version 1.0.2

"""
import csv
import os

from .api_requests import APIRequest
from .json_to_csv import JSONtoCSV 
from .city_database_finder import CityDataBaseFinder as cityFinder


class Recommendations():
    '''
    Clase con métodos para crear la lista de recomendaciones que se le entregará al usuario
    
    Métodos
    ---------
    * __init__(*args)
    * complete_atributes()
    * get_atributes()
    * get_number_atribute_Recommendation(file_name, atributeNo)
    * get_string_atribute_Recommentation(file_name, atributeNo)
    * get_recommendations()
    * limpiar_base_de_datos()
    
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
        self.header_atributes = []
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
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'Clima.csv')

        if self.noArgumentos == 1:
            if cityFinder.buscar_Ciudad(self.nombre_Ciudad):
               localizacion = cityFinder.get_Indice_Ciudad(self.nombre_Ciudad)
               self.header_atributes = cityFinder.get_Parametros(file_path, 0)
               self.atributes = cityFinder.get_Parametros(file_path, localizacion)
            else:
               nuevoJSON = APIRequest.get_formated_JSON(self.llave, 0, 0, self.nombre_Ciudad)
               if nuevoJSON is not None:
                   JSONtoCSV.append_JSON(nuevoJSON)
                   localizacion = cityFinder.get_Indice_Ciudad(self.nombre_Ciudad)
                   self.header_atributes = cityFinder.get_Parametros(file_path, 0)
                   self.atributes = cityFinder.get_Parametros(file_path, localizacion)
        else:
            if cityFinder.buscar_Coordenadas(self.latitud, self.longitud):
                localizacion = cityFinder.get_Indice_Coordenadas(self.latitud, self.longitud)
                self.header_atributes = cityFinder.get_Parametros(file_path, 0)
                self.atributes = cityFinder.get_Parametros(file_path, localizacion)
            else:
                nuevoJSON = APIRequest.get_formated_JSON(self.llave, self.latitud, self.longitud, "")
                if nuevoJSON is not None:
                    JSONtoCSV.append_JSON(nuevoJSON)
                    localizacion = cityFinder.get_Indice_Coordenadas(self.latitud, self.longitud)
                    self.header_atributes = cityFinder.get_Parametros(file_path, 0)
                    self.atributes = cityFinder.get_Parametros(file_path, localizacion)

    
    def get_atributes(self):
        """
        Método que devuelve la lista de atributos de un registro en Clima.csv
        
        Returns:
        recomendaciones (list): Lista que contiene todos los elementos de la fila de un registro en Clima.csv
        
        """
        formato_amigable = []

        if len(self.header_atributes) == len(self.atributes):
            for i in range(len(self.header_atributes)):
                formato_amigable.append(self.header_atributes[i].title() + ": " + self.atributes[i]) 
        
        return formato_amigable

      
    def get_number_atribute_Recomendation(self, file_name, atributeNo):
        """
        Método que devuelve la recomendacion dada por el Csv de recomendaciones de valores numericos

        Args:
        file_name (str): Nombre del csv con las recomendaciones
        atributeNo (int): Indice del valor del atributo

        Returns:
        recommendations (str): Cadena de recomendación

        """
        target_value = float(self.atributes[atributeNo])

        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file = os.path.join(base_dir, 'recomendTables', file_name+".csv")

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

    def get_string_atribute_Recomendation(self, file_name, atributeNo):
        """
        Método que devuelve la recomendacion dada por el Csv de recomendaciones de cadenas

        Args:
        file_name (str): Nombre del csv con las recomendaciones
        atributeNo (int): Indice del valor del atributo

        Returns:
        recommendations (str): Cadena de recomendación

        """
        target_value = self.atributes[atributeNo]

        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file = os.path.join(base_dir, 'recomendTables', file_name+".csv")
    
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
        weather_main = self.get_string_atribute_Recomendation("weather_main", 5)
        temp = self.get_number_atribute_Recomendation("temp", 6)
        feels_like = self.get_number_atribute_Recomendation("feels_like", 7)
        humidity = self.get_number_atribute_Recomendation("humidity", 8)
        wind_speed = self.get_number_atribute_Recomendation("wind_speed", 9)

        if temp == feels_like:
            self.recomendaciones = [weather_main, temp, humidity, wind_speed]
        else:
            self.recomendaciones = [weather_main, temp, feels_like, humidity, wind_speed]
        
        return self.recomendaciones

    def limpiar_base_de_datos():
        cityFinder.formatear_CSV()

        



        

    
    
    
