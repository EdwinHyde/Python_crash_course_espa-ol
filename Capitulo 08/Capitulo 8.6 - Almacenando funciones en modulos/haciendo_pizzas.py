import pizza    # Python abre el archivo pizza.py y copia todas las funciones
# Cualquier funcion creada en pizza.py estará disponible ahora en haciendo_pizza.py

# El llamado a la funcion se hace escribiendo el nombre del modulo importado(pizza)
# seguido por el nombre de la funcion hacer_pizza, separados por punto
# y enviando los argumentos necesarios para que funcione el programa.
pizza.hacer_pizza("mediana", "queso", "piña")
pizza.hacer_pizza("grande", "maicitos", "mortadela", "salchicha")
