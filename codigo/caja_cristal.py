import unittest

def es_mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class CajaCristalTest(unittest.TestCase):
    #O lo eres o no, entonces dos test
    def test_mayor_edad(self):
        edad=20

        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado, True)

    #segundo camino
    def test_es_menor(self):
        edad = 15

        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == "__main__":
    unittest.main()