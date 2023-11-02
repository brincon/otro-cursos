import unittest
import cambia_texto8

class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = cambia_texto8.todo_mayuscula(palabra)
        self.assertEqual(resultado, "BUEN DIA")

if __name__ == "__main__":
    unittest.main()

