# Se define la clase perro con la siguiente sentencia.
# En python el nombre de la clase debe ir la primera letra en mayuscula
# No hay parentesis en la definicion de la clase porque se crea desde cero.
class Perro:
    """Asi se modela un perro."""  # Docstring para describir lo que hace la clase
    # Las funciones dentro de las clases son llamadas metodos.
    def __init__(self, nombre, edad):  # __init__ es un metodo especial que se ejecuta automaticamente
        # El parametro self es requerido en la definicion del metodo y debe ir antes que los demas parametros.
        """Se inicializan los atributos de nombre y edad"""
        self.nombre = nombre
        self.edad = edad

    def sentarse(self):
        """Se hace la simulacion que un perro se siente como respuesta a un comando"""
        print(f"{self.nombre} ahora esta sentado.")

    def rodar(self):
        """Se hace la simulacion que el perro de vueltas como respuesta a un comando"""
        print(f"{self.nombre} se volteó")


mi_perro = Perro("pulgoso", 8)  # Se crea un perro cuyo nombre es pulgos y su edad 8 años
# El metodo __init__ crea una instancia representando este perro y pone los atributos de nombre y edad.
# usando los valores proporcionados. Pthon retorna una instancia que representa este perro

print(f"\nEl nombre de mi perro es {mi_perro.nombre.title()} y tiene {mi_perro.edad} años")
# Para acceder a los atributos de una instancia se usa la notacion de punto mi_perro.nombre
mi_perro.sentarse()  # Para llamar los metodos se escribe la instancia y el nombre del metodo separado por punto.
mi_perro.rodar()
# Esa instancia se la asignamos a la variable mi_perro.

el_perro_del_vecino = Perro("zeus", 2)  # Se pueden crear varias instancias


print(f"\nEl nombre del perro del vecino es {el_perro_del_vecino.nombre.title()} y tiene {el_perro_del_vecino.edad} años")
el_perro_del_vecino.sentarse()
el_perro_del_vecino.rodar()

