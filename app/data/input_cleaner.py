"""
Modulo Input Cleaner
Author: @ThePatrickCastle
Author: @C4mdax
Version 1.1.2

"""
import csv
import os

import unidecode

from rapidfuzz import process

class InputCleaner():
    '''
    Clase InputReader que limpia la cadena que ingresa el usuario

    Métodos
    -------
    * __init__(entradaUsuario)
    * get_lists(archivo_csv, nombre_columna)
    * get_results()
    * set_entrada_usuario(entradaNueva)
    * buscar_ciudad_con_IATA(iata)
    * quitar_acentos_de_array(lista)
    * encontrar_mejor_apareamiento()
    

    Atributos
    -------    
    * entradadUsuario (str): La cadena que ingresa el usuario en el buscador de la aplicacion 
    
    '''
    def __init__(self, entradaUsuario):
        """
        Metodo contructor de InputCleaner

        """
        self.entradaUsuario = entradaUsuario
        self.states = self.get_lists("IP2LOCATION-ISO3166-2.CSV", "subdivision_name")
        self.cities = self.get_lists("world-cities.csv", "name")
        self.iataCodes = self.get_lists("airports.csv", "code")
        self.cities_no_accents_array = self.quitar_acentos_de_array(self.cities)
        self.states_no_accents_array = self.quitar_acentos_de_array(self.states)
           

    def get_lists(self, archivo_csv, nombre_columna):
        """
        Metodo get_lists. Recoje los elementos de 2 archivos .csv para comparar sus elementos con la entrada de usuario
        
        Args:
        * archivo_csv (str): Nombre del archivo csv que se va a leer
        * nombre_columna (str): Nombre de la columna con los valores a comparar

        Returns:
        * elementos (list): Lista con todos los elementos en la comlumna nombre_columna del archivo_csv
        
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file = os.path.join(base_dir, 'finder', archivo_csv)

        elementos = []

        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)            
            for row in reader:
                elementos.append(row[nombre_columna])
        return elementos

    def get_results(self):
        """
        Método para regresar la lista de ciudades comparables para autocompletar la entrada de usuario

        Returns:
        * self.cities (list): Regresa la lista de ciudades con las que se compara la cadena usuario

        """
        return self.cities + self.states + self.iataCodes

    def set_entrada_usuario(self, nuevaEntrada):
        self.entradaUsuario = nuevaEntrada
    
    @staticmethod
    def buscar_ciudad_con_IATA(iata):
        """
        Metodo buscar_ciudad_con_IATA. Busca la ciudad cuyo aeropuerto tiene el codigo iata
        
        Args:
        * iata (str): Codigo iata a buscar

        Returns:
        * ciudad_row (str): Cadena con la ciudad del codigo iata
        
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file = os.path.join(base_dir, 'finder', 'airports.csv')

        with open(csv_file, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)               
            for row in reader:
                iata_row = row['code']
                ciudad_row = row['state']
                
                if iata_row == iata:
                    return ciudad_row                  
        return "No valid match found"
    
    def quitar_acentos_de_array(self, lista):
        """
        Metodo quitar_acentos_de_array. Regresamos un arreglo para comparar cadenas sin ningun acento.
        Args:
        * lista (list): De entrada

        Returns:
        * list: Lista de cadenas sin acentos

        """
        return [unidecode.unidecode(s) for s in lista]


    def encontrar_mejor_apareamiento(self):
        """
        Metodo encontrar_mejor_apareamiento. Usamos fastfuzz para encontrar el mejor raiting para la entrada del usuario
        
        Returns:
        * city_math[0] (str): La cadena con el nombre de la ciudad encontrada
        * buscar_ciudad_con_IATA(iata_match[0]) (str): El nombre de la ciudad referenciado del codigo IATA        
        """
        cities_no_accents = process.extractOne(self.entradaUsuario.title(), self.cities_no_accents_array)
        states_no_accents = process.extractOne(self.entradaUsuario.title(), self.states_no_accents_array)
        cities_pure_match = process.extractOne(self.entradaUsuario, self.cities)
        state_pure_match = process.extractOne(self.entradaUsuario, self.states)
        cities_match = process.extractOne(self.entradaUsuario.title(), self.cities)
        state_match = process.extractOne(self.entradaUsuario.title(), self.states)
        iata_match = process.extractOne(self.entradaUsuario.upper(), self.iataCodes)

        results = {
            'cities_no_accents': (cities_no_accents[0], cities_no_accents[1]) if cities_no_accents[1] >= 91 else (None, 0),
            'states_no_accents': (states_no_accents[0], states_no_accents[1]) if states_no_accents[1] >= 91 else (None, 0),
            'city_pure': (cities_pure_match[0], cities_pure_match[1]) if cities_pure_match[1] >= 91 else (None, 0),
            'state_pure': (state_pure_match[0], state_pure_match[1]) if state_pure_match[1] >= 91 else (None, 0),
            'city': (cities_match[0], cities_match[1]) if cities_match[1] >= 91 else (None, 0),
            'state': (state_match[0], state_match[1]) if state_match[1] >= 91 else (None, 0),
            'iata': (self.buscar_ciudad_con_IATA(iata_match[0]), iata_match[1]) if iata_match[1] >= 91 and self.buscar_ciudad_con_IATA(iata_match[0]) != "" else (None, 0)
        }
        
        best_match_type, (best_name, best_score) = max(results.items(), key=lambda x: x[1][1])
        
        if best_name:
            return best_name
        return "No valid match found"



    
