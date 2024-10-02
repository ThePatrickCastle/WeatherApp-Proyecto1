"""
Modulo para buscar Ciudades en la base de datos.
Author: @ThePatrickCastle
Version 1.0.2

"""
import os
import csv

class CityDataBaseFinder:
    '''
    Clase que determina si una ciudad está o no en la base de datos Clima.csv

    Métodos
    -------
    * buscar_Ciudad(ciudad)
    * get_Indice_Ciudad(ciudad)
    * buscar_Coordenadas(latitud, longitud)
    * get_Indice_Coordenadas(latitud, longitud)
    * get_Parametro(row_index, file_path)
    * formatear_CSV()
    
    '''
    @staticmethod
    def buscar_Ciudad(ciudad):
        """
        Método buscar la ciudad en la base de datos Clima.csv
        
        Args:
        ciudad (str): La ciudad que buscaremos

        Returns:
        (bool): Falso si no está en el Clima.csv y verdadero si está en el Clima.csv
        
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'Clima.csv')

        archivo_existente = os.path.isfile(file_path)

        if not archivo_existente:
            return False
        else:
            with open(file_path, 'r', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    if row["ciudad"] == ciudad or row["name"] == ciudad:
                        return True
                return False

    @staticmethod
    def get_Indice_Ciudad(ciudad):
        """
        Método que regresa el indice de una ciudad en Clima.csv
        
        Args:
        ciudad (str): La ciudad que buscaremos

        Returns:
        row_index (int): Regresa el indice de la ciudad o -1 si no la encuentra
        
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'Clima.csv')

        archivo_existente = os.path.isfile(file_path)
        if not archivo_existente:
            return -1
        else:
            with open(file_path, 'r', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row_index, row in enumerate(reader):
                    row_index += 1
                    if row["ciudad"] == ciudad or row["name"] == ciudad:
                        return row_index
            return -1

    @staticmethod
    def buscar_Coordenadas(latitud, longitud):
        """
        Método para buscar una latitud y longitud en la base de datos Clima.csv
        
        Args:
        latitud (double): Primer parametro para busqueda por coordenadas
        longitud (double): Segundo parametro para busqueda por coordenadas

        Returns:
        (bool): Falso si no está en el Clima.csv y verdadero si está en el Clima.csv
        
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'Clima.csv')

        archivo_existente = os.path.isfile(file_path)
        if not archivo_existente:
            return False
        else:
            with open(file_path, mode='r') as csv_file:
                reader = csv.DictReader(csv_file)               
                found = False
                for row in reader:
                    lat = float(row['lat'])
                    lon = float(row['lon'])
                    
                    if lat == latitud and lon == longitud:
                        found = True                   
                return found

    @staticmethod
    def get_Indice_Coordenadas(latitud, longitud):
        """
        Método que regresa el indice de cierta latitud y longitud
        
        Args:
        latitud (double): Primer parametro para busqueda por coordenadas
        longitud (double): Segundo parametro para busqueda por coordenadas

        Returns:
        row_index (int): Regresa el indice de la longitud donde esté la latitud y longitud correspondiente o -1 si no los encuentra
        
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'Clima.csv')

        archivo_existente = os.path.isfile(file_path)
        if not archivo_existente:
            return -1
        else:
            with open(file_path, mode='r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row_index, row in enumerate(reader):
                    row_index += 1
                    lat = float(row['lat'])
                    lon = float(row['lon'])
                    
                    if lat == latitud and lon == longitud:
                        return row_index
            return -1
   
    @staticmethod
    def get_Parametros(path_file, row_index):
        """
        Método que, dado el indice, regresa una lista con todos los parametros de una ciudad.
        
        Args:
        path_file (str): Archivo en el que se buscará el archivo
        row_index (int): Indice donde se buscará
        
        Returns:
        rows[row_index] (lista): Lista de los elementos en un indice
        
        """
        archivo_existente = os.path.isfile(path_file)
        if not archivo_existente:
            return False
        else:
            with open(path_file, mode='r') as file:
                reader = csv.reader(file)
                rows = list(reader)
                if 0 <= row_index < len(rows):
                    return rows[row_index]
                else:
                    return []
                        
    @staticmethod
    def formatear_CSV():
        """
        Método que formatea la base de datos Clima.csv menos su header

        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'Clima.csv')

        archivo_existente = os.path.isfile(file_path)
        if not archivo_existente:
            pass
        else:
            with open(file_path, 'r', newline='') as csv_file:
                reader = csv.reader(csv_file)
                header = next(reader)
            
                with open(file_path, 'w', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(header)
                

                
           
