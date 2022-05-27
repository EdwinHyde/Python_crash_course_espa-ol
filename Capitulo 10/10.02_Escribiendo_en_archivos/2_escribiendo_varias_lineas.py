nombre_de_archivo = "programando2.txt"  # Si el archivo existe, será sobreescrito.

with open(nombre_de_archivo, 'w') as file_object:
    file_object.write("Me gusta programar.\n")
    file_object.write("Me gusta mucho aprender.\n")  # al agregar esta linea de texto, no se hará en una nueva linea
    # esta linea se hará enseguida de la linea anterior quedando t o d o en una sola linea de texto, por esto se usa
    # \n para crear el salto de linea. Tambien es posible usar espacios y tabuladores para formatear la salida.