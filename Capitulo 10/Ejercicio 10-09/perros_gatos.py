# 10-9. Silent Cats and Dogs:
# Modify your except block in Exercise 10-8 to fail silently if either file is missing.

gatos = 'gatos.txt'
perros = 'perros.txt'

def mostrar_mascotas(mascotas):
    try:
        with open(mascotas, encoding='utf-8') as f:
            contenido = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contenido)

mascotas = ['gatos.txt', 'perros.txt']
for mascota in mascotas:
    mostrar_mascotas(mascota)