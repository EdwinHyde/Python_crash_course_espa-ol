# Este archivo abrirá un archivo externo, en este caso numeros_pi.txt, ubicado en la misma carpeta.

# La funcion open() necesita un argumento, el nombre del archivo que se quiere abrir.
# Python busca el archivo en el directorio donde se ejecuta el programa y busca el archivo externo en la carpeta.
# La funcion open() retorna un objeto que representa al archivo (numeros_pi.txt) y python lo asigna a "archivo"

with open('numeros_pi.txt') as archivo:  # "with" cierra el archivo una vez que ya no es necesario acceder a él.
    contenido = archivo.read()  # usamos el metodo read() para leer el contenido completo del archivo y guadarlo
    # como una cadena larga en la variable contenido
print(contenido.rstrip())  # se imprime el valor de contenido, recuperando todo el texto del archivo.