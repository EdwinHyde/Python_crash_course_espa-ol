# 10-8. Cats and Dogs:
# Make two files, cats.txt and dogs.txt.
# Store at least three names of cats in the first file and three names of dogs in the second file.
# Write a program that tries to read these files and print the contents of the file to the screen.
# Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing.
# Move one of the files to a different location on your system,
# and make sure the code in the except block executes properly.

# 1. Se crean dos archivos gatos.txt y perros.txt
gatos = 'gatos.txt'
perros = 'perros.txt'

# 2. Se ingresan varios nombres de gatos y de perros
with open(gatos, 'a', encoding='utf-8') as f:
    f.write('\nangora')
    f.write('\nEgipcio')
    f.write('\nMichi')

# with open(perros, 'a', encoding='utf-8') as f:
#     f.write('\nsiberiano')
#     f.write('\nboxer')
#     f.write('\npulgoso')

def mostrar_mascotas(mascotas):
    try:
        with open(mascotas, encoding='utf-8') as f:
            contenido = f.read()
    except FileNotFoundError:
        print(f'Lo siento, no se encuentra el archivo {mascotas} en la ubicacion especificada.')
    else:
        print(contenido)

mascotas = ['gatos.txt', 'perros.txt']
for mascota in mascotas:
    mostrar_mascotas(mascota)


# archivo1 = 'perros.txt'
# archivo2 = 'gatos.txt'
#
# print("Perros".center(30, '-'))
# try:
#     with open(archivo1, encoding='utf-8') as f:
#         contenido = f.read()
# except FileNotFoundError:
#     print(f'Lo siento, no encontramos el archivo {archivo1}')
#
# else:
#     print(contenido)
#
# print()
# print("Gatos".center(30, '-'))
# try:
#     with open(archivo2, encoding='utf-8') as f:
#         contenido = f.read()
# except FileNotFoundError:
#     print(f'Lo siento, no encontramos el archivo {archivo2}')
#
# else:
#     print(contenido)
