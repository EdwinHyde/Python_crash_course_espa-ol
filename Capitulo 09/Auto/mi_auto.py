from auto import Carro
# Se importa la clase Carro desde el modulo auto.py. Ahora es posible usar la clase como si estuviera definida
# en este archivo. Similar a lo visto en importar funciones

mi_auto_nuevo = Carro("toyota", "prado", "2022")
print(f"Los datos del auto nuevo son:\n{mi_auto_nuevo.nombre_descriptivo()}" )

mi_auto_nuevo.lectura_odometro = 23
mi_auto_nuevo.leer_odometro()

