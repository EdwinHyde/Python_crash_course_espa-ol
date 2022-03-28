# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
#           In each dictionary, include the kind of animal and the owner’s name.
#           Store these dictionaries in a list called pets. Next, loop through your list and as
#           you do, print everything you know about each pet.

pulgoso = {'animal': 'perro', 'dueño': 'chavela'}
minino = {'animal': 'gato', 'dueño': 'aleja'}
zeus = {'animal': 'gallo', 'dueño': 'jero'}

mascotas = [pulgoso, minino, zeus]

for mascota in mascotas:
    print(f"La mascota es un {mascota['animal']}, y el dueño es: {mascota['dueño'].title()}")

