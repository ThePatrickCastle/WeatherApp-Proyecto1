"""
Modulo para guardar JSON formateados a Clima.csv 
Author: @ThePatrickCastle
Version 1.0.1

"""

import os
import csv

class JSONtoCSV:
    '''
    Clase con métodos para transformar un JSON a un CSV
    
    Métodos
    -------
    * verificar_Entrada_en_CSV(jsonData)
    * append_JSON(jsonData)
    
    ''' 
    @staticmethod
    def verificar_Entrada_en_CSV(jsonData):
        """
        Método para verificar si la columna que queremos agregar no existe en Clima.csv anteriormente
        
        Args:
        jsonData (diccionario): El conjunto de datos que queremos revisar si ya está en Clima.csv

        Returns:
        (bool): Verdadero si es que no está en el Clima.csv, y falso si está en el Clima.csv
        
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'Clima.csv')

        ciudad = jsonData.get("name")
        with open(file_path, 'r', newline='', encoding = 'utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row["name"] == ciudad:
                    return False
        return True

    @staticmethod
    def append_JSON(jsonData):
        """
        Método para agregar un informacion de un diccionario a Clima.csv
        
        Args:
        jsonData (diccionario): El conjunto de datos que queremos agregar a Clima.csv
        
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'Clima.csv')

        archivo_existente = os.path.isfile(file_path)
        
        keys = jsonData.keys()
        values = jsonData.values()
        
        with open(file_path, 'a', newline = '', encoding = 'utf-8') as csv_file:
            writer = csv.writer(csv_file)
            
            if not archivo_existente:
                writer.writerow(keys)

            if JSONtoCSV.verificar_Entrada_en_CSV(jsonData):
                writer.writerow(values)

