from fuzzywuzzy import process

class InputCorrector:
    '''
    Clase que encuentra la mejor coincidencia de una cadena dada una lista de cadenas.
    
    Métodos
    -------
    * encuentra_coincidencia(cadena, lista)
    '''
    def encuentra_coincidencia(self, cadena, lista):  # Añadí 'self' como primer argumento
        mejor_coincidencia = process.extractOne(cadena, lista)

        if mejor_coincidencia:
            return mejor_coincidencia[0]
        else:
            return None
