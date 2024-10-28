import unittest

# pruebas de caja negra
def suma(num_1, num_2):
    return num_1 + num_2


class CanaNegraTest(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num_1= 10
        num_2 = 6
        resultado = suma( num_1,num_2)
        
        self.assertEqual(resultado, 16)
        
        
    def test_suma_negativos(self):
        num_1 = -10
        num_2 = -6
        resultado = suma(num_1,num_2)
        
        self.assertEqual(resultado, -16)
        
        
        if __name__ == "__main__" :
            unittest.main(verbosity=2)