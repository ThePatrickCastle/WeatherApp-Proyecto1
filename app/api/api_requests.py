"""
Modulo de Requests
Autor: @ThePatrickCastle
Version 1.0.2

"""

import requests

class APIRequest():
    '''
    Clase con métodos para trabajar con la API de Open Weather Map que contiene el archivo json que devuelve el API.
    
    Métodos
    -------
    * request_JSON(llave, latitud, longitud, ciudad)
    * get_formated_JSON(llave, latitud, longitud, ciudad)
    
    '''

    @staticmethod
    def request_JSON(llave, latitud, longitud, ciudad):
        """
        Método para llamar a la API

        Args:
        llave (str): Llave de licencia de OpenWeatherMap
        latitud (double): Coordenada 1 para hacer request por coordenadas
        longitud (double): Coordenada 2 para hacer request por coordenadas
        ciudad (str): Cadena para buscar en el request. Debe estar verificada primero desde entrada de usuario

        Returns: 
        jsonData.json() (json): Regresa un archivo de texto con formato json
        
        """
        if ciudad == "":
            try:
                jsonData = requests.get(
                    f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={llave}")
            except requests.ConnectionError as e:
                print(f"Connection error: {e}")
                return None
            except Exception as e:
                print(f"Request Failed. Status Code: {jsonData.status_code}")
                return None
            
            if not jsonData.ok:
                print(f"Request Failed. Status Code: {jsonData.status_code}")
            
            return jsonData.json()
        else:
            try:
                jsonData = requests.get(
                    f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={llave}")
            except requests.ConnectionError as e:
                print(f"Connection error: {e}")
                return None
            except Exception as e:
                print(f"Request Failed. Status Code: {jsonData.status_code}")
                return None
            
            if not jsonData.ok:
                print(f"Request Failed. Status Code: {jsonData.status_code}")
            
            return jsonData.json()
            


    @staticmethod
    def get_formated_JSON(llave, latitud, longitud, ciudad):
        """
        Método para extraer un diccionario del JSON respuesta

        Args:
        llave (str): Llave de licencia de OpenWeatherMap
        latitud (double): Coordenada 1 para hacer request por coordenadas
        longitud (double): Coordenada 2 para hacer request por coordenadas
        ciudad (str): Cadena para buscar en el request. Debe estar verificada primero desde entrada de usuario

        Returns: 
        climaCiudad (diccionario): Regresa un diccionario con los datos de interés que estaban en el JSON
        
        """
        jsonData = APIRequest.request_JSON(llave, latitud, longitud, ciudad)

        if jsonData is None:
            return None 

        climaCiudad = {
            "ciudad": ciudad,
            "country": jsonData["sys"]["country"],
            "name": jsonData["name"],
            "lat": jsonData["coord"]["lat"],
            "lon": jsonData["coord"]["lon"],
            "weather_main": jsonData["weather"][0]["main"],
            "temp": jsonData["main"]["temp"],
            "feels_like": jsonData["main"]["feels_like"],
            "humidity": jsonData["main"]["humidity"],
            "wind_speed": jsonData["wind"]["speed"]
        }
        
        return climaCiudad

    
