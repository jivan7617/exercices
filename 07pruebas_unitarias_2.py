import unittest
# pruebas de caja de cristal

# enesta prueba se verifica el codigo paso a pase implementando condiciones que se cumplan y que no se cumplan para ver si el codigo esta bien escrito


def es_mayor(edad):
    if edad >= 18:
        return True
    
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    def test_es_mayor(self):
        edad =19
        resultado = es_mayor(edad)
        self.assertEqual(resultado, True)
        
    def test_es_mayor_T(self):
        edad =18
        resultado = es_mayor(edad)
        self.assertEqual(resultado, True)
        
    def test_es_menor(self):
        edad = 15
        resultado = es_mayor(edad)
        self.assertEqual(resultado, False)





if __name__ == "__main__":
    unittest.main()