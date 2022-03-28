# 6-1. Person: Use a dictionary to store information about a person you know.
#       Store their first name, last name, age, and the city in which they live. You
#       should have keys such as first_name, last_name, age, and city. Print each
#       piece of information stored in your dictionary.

persona = {
    "nombre": "andrea",
    'apellido': 'pérez',
    'edad': 33,
    'ciudad': 'dorada'
    }

print(persona["nombre"].title())
print(persona["apellido"].title())
print(persona['edad'])
print(persona["ciudad"].title())
