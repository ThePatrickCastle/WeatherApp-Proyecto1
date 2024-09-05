"""
Modulo para guardar JSON formateados a Clima.csv 
Author: @ThePatrickCastle
Version 1.0

"""

import os
import csv

class JSONtoCSV:
    '''
    Clase con métodos para transformar un JSON a un CSV
    
    Métodos
    -------
    * verificarEntrada(jsonData)
    * appendJSON(jsonData)
    
    ''' 
    @staticmethod
    def verificarEntradaenCSV(jsonData):
        """
        Método para verificar si la columna que queremos agregar no existe en Clima.csv anteriormente
        
        Args:
        jsonData (diccionario): El conjunto de datos que queremos revisar si ya está en Clima.csv

        Returns:
        (bool): Verdadero si es que no está en el Clima.csv, y falso si está en el Clima.csv
        
        """
        ciudad = jsonData.get("name")
        with open("./Clima.csv", 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row["name"] == ciudad:
                    return False
        return True

    @staticmethod
    def appendJSON(jsonData):
        """
        Método para agregar un informacion de un diccionario a Clima.csv
        
        Args:
        jsonData (diccionario): El conjunto de datos que queremos agregar a Clima.csv
        
        """
        archivo_existente = os.path.isfile("./Clima.csv")
        
        keys = jsonData.keys()
        values = jsonData.values()
        
        with open("./Clima.csv", 'a', newline = '') as csv_file:
            writer = csv.writer(csv_file)
            
            if not archivo_existente:
                writer.writerow(keys)

            if JSONtoCSV.verificarEntradaenCSV(jsonData):
                writer.writerow(values)

