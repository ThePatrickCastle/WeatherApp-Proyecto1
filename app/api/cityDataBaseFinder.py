"""
Modulo para buscar Ciudades en la base de datos.
Author: @ThePatrickCastle
Version 1.0

"""
import os
import csv

class CityDataBaseFinder:
    '''
    Clase que determina si una ciudad está o no en la base de datos Clima.csv

    Métodos
    -------
    * buscarCiudad(ciudad)
    * getIndiceCiudad(ciudad)
    * buscarCoordenadas(latitud, longitud)
    * getIndiceCoordenadas(latitud, longitud)
    * getParametro(row_index)
    * formatearCSV()
    
    '''
    @staticmethod
    def buscarCiudad(ciudad):
        """
        Método buscar la ciudad en la base de datos Clima.csv
        
        Args:
        ciudad (str): La ciudad que buscaremos

        Returns:
        (bool): Falso si no está en el Clima.csv y verdadero si está en el Clima.csv
        
        """
        archivo_existente = os.path.isfile("./Clima.csv")
        if not archivo_existente:
            return False
        else:
            with open("./Clima.csv", 'r', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    if row["name"] == ciudad:
                        return True
                return False

    @staticmethod
    def getIndiceCiudad(ciudad):
        """
        Método que regresa el indice de una ciudad en Clima.csv
        
        Args:
        ciudad (str): La ciudad que buscaremos

        Returns:
        row_index (int): Regresa el indice de la ciudad o -1 si no la encuentra
        
        """
        archivo_existente = os.path.isfile("./Clima.csv")
        if not archivo_existente:
            return -1
        else:
            with open("./Clima.csv", 'r', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row_index, row in enumerate(reader):
                    row_index += 1
                    if row["name"] == ciudad:
                        return row_index
            return -1

    @staticmethod
    def buscarCoordenadas(latitud, longitud):
        """
        Método para buscar una latitud y longitud en la base de datos Clima.csv
        
        Args:
        latitud (double): Primer parametro para busqueda por coordenadas
        longitud (double): Segundo parametro para busqueda por coordenadas

        Returns:
        (bool): Falso si no está en el Clima.csv y verdadero si está en el Clima.csv
        
        """
        archivo_existente = os.path.isfile("./Clima.csv")
        if not archivo_existente:
            return False
        else:
            with open("./Clima.csv", mode='r') as csv_file:
                reader = csv.DictReader(csv_file)               
                found = False
                for row in reader:
                    lat = float(row['lat'])
                    lon = float(row['lon'])
                    
                    if lat == latitud and lon == longitud:
                        found = True                   
                return found

    @staticmethod
    def getIndiceCoordenadas(latitud, longitud):
        """
        Método que regresa el indice de cierta latitud y longitud
        
        Args:
        latitud (double): Primer parametro para busqueda por coordenadas
        longitud (double): Segundo parametro para busqueda por coordenadas

        Returns:
        row_index (int): Regresa el indice de la longitud donde esté la latitud y longitud correspondiente o -1 si no los encuentra
        
        """
        archivo_existente = os.path.isfile("./Clima.csv")
        if not archivo_existente:
            return -1
        else:
            with open("./Clima.csv", mode='r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row_index, row in enumerate(reader):
                    row_index += 1
                    lat = float(row['lat'])
                    lon = float(row['lon'])
                    
                    if lat == latitud and lon == longitud:
                        return row_index
            return -1
   
    @staticmethod
    def getParametros(row_index):
        """
        Método que, dado el indice, regresa una lista con todos los parametros de una ciudad.
        
        Args:
        row_index
        
        Returns:
        rows[row_index] (lista): Lista de los elementos en un indice
        
        """
        archivo_existente = os.path.isfile("./Clima.csv")
        if not archivo_existente:
            return False
        else:
            with open("./Clima.csv", mode='r') as file:
                reader = csv.reader(file)
                rows = list(reader)
                if 0 <= row_index < len(rows):
                    return rows[row_index]
                else:
                    return []
        
    @staticmethod
    def formatearCSV():
        """
        Método que formatea la base de datos Clima.csv menos su header

        """
        with open("./Clima.csv", 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            
            with open("./Clima.csv", 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header)
                

                
           
