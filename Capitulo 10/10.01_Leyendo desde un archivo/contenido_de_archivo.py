# TRABAJANDO CON EL CONTENIDO DE UN ARCHIVO.

nombre_archivo = ('numeros_pi.txt')

with open(nombre_archivo) as file_object:
    lineas = file_object.readlines()

texto_string = ''
for linea in lineas:
    texto_string += linea.strip()

print(texto_string)
print(len(texto_string))