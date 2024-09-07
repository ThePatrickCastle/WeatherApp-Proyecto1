"""
Modulo Input Cleaner
Author: @ThePatrickCastle
Author: @C4mdax
Version 1.0.2

"""
import csv

from rapidfuzz import process

class InputCleaner():
    '''
    Clase InputReader que limpia la cadena que ingresa el usuario

    Métodos
    -------
    * __init__(entradaUsuario)
    * get_lists(archivo_csv, nombre_columna)
    * set_entrada_usuario(entradaNueva)
    * buscar_ciudad_con_IATA(iata)
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
           

    def get_lists(self, archivo_csv, nombre_columna):
        """
        Metodo get_lists. Recoje los elementos de 2 archivos .csv para comparar sus elementos con la entrada de usuario
        
        Args:
        * archivo_csv (str): Nombre del archivo csv que se va a leer
        * nombre_columna (str): Nombre de la columna con los valores a comparar

        Returns:
        * elementos (list): Lista con todos los elementos en la comlumna nombre_columna del archivo_csv
        
        """
        elementos = []
        with open("./data/finder/"+archivo_csv, mode='r') as file:
            reader = csv.DictReader(file)            
            for row in reader:
                elementos.append(row[nombre_columna])
        return elementos

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
        with open("./data/finder/airports.csv", mode='r') as csv_file:
            reader = csv.DictReader(csv_file)               
            for row in reader:
                iata_row = row['code']
                ciudad_row = row['state']
                
                if iata_row == iata:
                    return ciudad_row                  
        return "No valid match found"
    
    def encontrar_mejor_apareamiento(self):
        """
        Metodo encontrar_mejor_apareamiento. Usamos fastfuzz para encontrar el mejor raiting para la entrada del usuario
        
        Returns:
        * city_math[0] (str): La cadena con el nombre de la ciudad encontrara
        * buscar_ciudad_con_IATA(iata_match[0]) (str): El nombre de la ciudad referenciado del codigo IATA       
        
        """
        cities_match = process.extractOne(self.entradaUsuario.title(), self.cities)
        state_match = process.extractOne(self.entradaUsuario.title(), self.states)
        iata_match = process.extractOne(self.entradaUsuario.upper(), self.iataCodes)
        
        if cities_match[1] and iata_match[1] and state_match[1] and max(cities_match[1], state_match[1], iata_match[1]) >= 91:
            best_match = max(cities_match[1], state_match[1], iata_match[1])
            if cities_match[1] == best_match:
                return cities_match[0]
            elif state_match[1] == best_match:
                return state_match[0]
            else:
                return self.buscar_ciudad_con_IATA(iata_match[0])
        elif cities_match[1] and iata_match[1] and max(cities_match[1], iata_match[1]) >= 91:
            if cities_match[1] > iata_match[1]:
                return cities_match[1]
            else:
                return self.buscar_ciudad_con_IATA(iata_match)
        elif cities_match[1] and state_match[1] and max(cities_match[1], state_match[1]) >= 91:
            if cities_match[1] > state_match[1]:
                return cities_match[0]
            else:
                return state_match[0]
        elif state_match[1] and iata_match[1] and max(state_match[1], iata_match[1]) >= 91:
            if states_match[1] > iata_match[1]:
                return states_match[0]
            else:
                return self.buscar_ciudad_con_IATA(iata_match[0])
        elif cities_match[1] >= 91:
            return cities_match[0]
        elif state_match[1] >= 91:
            return state_match[0]
        elif iata_match[1] >= 91:
            return self.buscar_ciudad_con_IATA(iata_match[0])
        else:
            return "No valid match found"


    
