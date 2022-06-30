# Para escribir un caso de pruebas para una funcion, se debe importar el modulo unittest y la funcion que se
# quiere testear, Luego se crea una clase que herede de unittest.Testcase, y escribir una serie de metodos para probar
# los diferentes aspectos del comportamiento de su función.
# Aquí hay una caso de pruebas con un metodo que verifica que la funcion obtener_nombre_formateado() trabaje de forma
# correcta cuando se le da un nombre  un apellido.

import unittest  # Se importa el modulo unittest
from L1_testing import obtener_nombre_formateado  # Se importa la funcion que queremos probar la cual tendrá una serie
# de pruebas unitarias.

class NombresTestCase(unittest.TestCase):  # Se crea una clase que herede desde unittest.TestCase
    # Es recomendable nombrar la clase con un nombre relacionado a la funcion que se quiere probar y hacer uso de
    # la palabra Test en el nombre de la clase.
    """Pruebas para la funcion testing.py"""

    def test_nombre_apellido(self):  # Creamos la funcion
        """Funcionan nombres como 'Joaquin Sabina'?"""
        nombre_formateado = obtener_nombre_formateado("Joaquin", "Sabina") # Llamamos la funcion que queremos probar
        # en este caso llamamos obtener_nombre_formateado() con los argumentos "joaquin" y "sabina" y asignamos el
        # resultado a nombre_formateado.

        self.assertEqual(nombre_formateado, 'Joaquin Sabina')  # Se hace uso de una de las caracteristicas mas utiles
        # de unittest, un metodo assert. Los métodos assert verifican que un resultado que recibió
        # coincida con el resultado que esperaba recibir.
        # Para verificar si es verdadero usamos el metodo assertEqual() y le pasamos la variable nombre_formateado,
        # y "Joaquin Sabina". La linea dice: compare los valores en nombre_formateado con la cadena "Joaquin Sabina"
        # Si son iguales como esperamos, bien, pero si no coinciden, hazmelo saber.


# Es importante tener en cuenta que muchos frameworks importan sus archivos de prueba antes de ejecutarlos.
# Cuando se importa un archivo, el intérprete ejecuta el archivo a medida que se importa.

if __name__ == "__main__":  # El bloque if busca una variable especial, __name__, que se establece cuando se ejecuta
    # el programa. Si este archivo se ejecuta como el programa principal, el valor de __name__
    # se establece en '__main__'.
    unittest.main  # En este caso, llamamos a unittest.main(), que ejecuta el caso de prueba.
    # Cuando un framework importa este archivo, el valor de __name__ no será '__main__' y este bloque no se ejecutará.