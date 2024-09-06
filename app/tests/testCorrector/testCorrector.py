# tests/testCorrector/testCorrector.py
import unittest
import sys
import os

# Añadir la carpeta 'data' al path para que Python pueda encontrar 'corrector.py'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data')))

from inputCorrector import encuentra_coincidencia

class TestEncuentraCoincidencia(unittest.TestCase):

    def test_coincidencia_exacta(self):
        lista = ["ejemplo", "exemplo", "ejemplo1", "ejem"]
        resultado = encuentra_coincidencia("ejemplo", lista)
        self.assertEqual(resultado, "ejemplo")

    def test_coincidencia_parcial(self):
        lista = ["ejemplo", "exemplo", "ejemplo1", "ejem"]
        resultado = encuentra_coincidencia("ejem", lista)
        self.assertEqual(resultado, "ejem")

    def test_coincidencia_sin_resultado(self):
        lista = ["ejemplo", "exemplo", "ejemplo1", "ejem"]
        resultado = encuentra_coincidencia("noexistente", lista)
        self.assertIsNone(resultado)

    def test_coincidencia_con_lista_vacia(self):
        lista = []
        resultado = encuentra_coincidencia("ejemplo", lista)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
