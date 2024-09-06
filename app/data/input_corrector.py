from fuzzywuzzy import process
class InputCorrector:
    '''
    Clase que encuentra la mejor coincidencia de una cadena dada una lista de cadenas.
    
    Métodos
    -------
    * encuentra_ciudad(cadena, lista)
    '''
    def encuentra_coincidencia(cadena, lista):
        mejor_coincidencia = process.extractOne(cadena, lista)

        if mejor_coincidencia:
            return mejor_coincidencia[0]
        else:
            return None

