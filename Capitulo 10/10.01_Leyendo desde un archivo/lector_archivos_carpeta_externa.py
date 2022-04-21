# ABRIR ARCHIVOS DESDE UNA CARPETA DIFERENTE A LA RAIZ.

with open('archivos_texto/texto_externo.txt') as archivo:  # Se le da la ruta a python del archivo que se quiere abrir.
    contenido = archivo.read()
print(contenido.rstrip())


# RUTA ABSOLUTA DE ARCHIVO.

# Se puede indicar a python donde se encuentra exactamente el archivo en el computador
# en lugar de buscar en la ruta donde se ejecuta el programa.
# Como estas rutas son tan largas, es recomendable asignarla a una variable y luego pasarla la variable con el
# método open():
ruta_de_archivo = "D:/Brave.txt"
with open(ruta_de_archivo) as otro_archivo:
    print(otro_archivo)
