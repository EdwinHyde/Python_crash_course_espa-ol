# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
#           Make two new dictionaries representing different people, and store all three
#           dictionaries in a list called people. Loop through your list of people. As you
#           loop through the list, print everything you know about each person.

persona_1 = {
    "nombre": "andrea",
    'apellido': 'pérez',
    'edad': '33',
    'ciudad': 'dorada',
    }

persona_2 = {
    "nombre": "edwin",
    'apellido': 'chica',
    'edad': '40',
    'ciudad': 'palocabildo',
    }

persona_3 = {
    "nombre": "alejandra",
    'apellido': 'chica',
    'edad': '35',
    'ciudad': 'villahermosa',
    }

personas = [persona_1, persona_2, persona_3]
for persona in personas:
    for k, v in persona.items():
        print(f'Los datos son: {k.title()} = {v.title()}')
    print("")
