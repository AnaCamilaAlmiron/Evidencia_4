import unittest
from unittest.mock import patch
from evidencia_4 import MaquinaHacerVelas

class TestMaquinaHacerVelas(unittest.TestCase):
    def setUp(self):
        # Creamos dos instancias para pruebas: una con parametros correctos y otra con parametros incorrectos.
        self.prueba_correcta = MaquinaHacerVelas(True, "rojo", True)
        self.prueba_incorrecta = MaquinaHacerVelas(False, "azul", False)
        
    
    def test_derretir_cera_correcto(self):
        # Caso cuando se puede derretir la cera.
        resultado = self.prueba_correcta.derretir_cera()
        self.assertEqual(resultado, "La cera llegó a 80 grados, por lo cual se derritió por completo.")
    
    def test_derretir_cera_incorrecto(self):
        # Caso cuando no se puede derretir la cera.
        resultado = self.prueba_incorrecta.derretir_cera()
        self.assertEqual(resultado, "La máquina no puede derretir la cera, controlar la temperatura.")
    
    def test_insertar_color_correcto(self):
        # Caso cuando se inserta el color correcto (rojo).
        resultado = self.prueba_correcta.insertar_color()
        self.assertEqual(resultado, "El color que has insertado es rojo, por lo cual se puede continuar con el proceso.")
    
    def test_insertar_color_incorrecto(self):
        # Caso cuando se inserta un color incorrecto (no rojo).
        resultado = self.prueba_incorrecta.insertar_color()
        self.assertEqual(resultado, "El color que has insertado es {self.color}, por lo cual no se puede continuar con el proceso.")
    
    def test_verter_cera_correcto(self):
        # Caso cuando está listo para verter la cera.
        resultado = self.prueba_correcta.verter_cera_molde()
        self.assertEqual(resultado, "Está listo para verter la cera en los moldes.")
    
    def test_verter_cera_incorrecto(self):
        # Caso cuando no está listo para verter la cera.
        resultado = self.prueba_incorrecta.verter_cera_molde()
        self.assertEqual(resultado, "No está listo para verter la cera al molde. Controlar si la cera está a temperatura correcta.")
        
        

if __name__ == "__main__":
    unittest.main()
