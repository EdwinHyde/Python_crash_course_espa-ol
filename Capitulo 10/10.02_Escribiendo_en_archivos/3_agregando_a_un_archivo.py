nombre_de_archivo = "programando2.txt"

# Si queremos agregar contenido al archivo en lugar de escribir sobre el contenido existente, abrimos el archivo
# en modo append 'a'.
# Python no borra el contenido del archivo, las lineas agregadas seran escritas al final del archivo.
# Si el archivo no existe, se creara un archivo vacio.

with open(nombre_de_archivo, 'a') as file_object:  # usamos el argumento 'a' para agregar informacion
    file_object.write("Aunque me ha costado bastante tiempo es genial.\n")  # se agrega el contenido deseado.
    file_object.write("Me gustaría seguir aprendiendo sin parar.\n")