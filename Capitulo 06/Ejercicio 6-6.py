# 6-6. Polling: Use the code in favorite_languages.py (page 97).
#       •	 Make a list of people who should take the favorite languages poll. Include
#           some names that are already in the dictionary and some that are not.
#       •	 Loop through the list of people who should take the poll. If they have
#           already taken the poll, print a message thanking them for responding.
#           If they have not yet taken the poll, print a message inviting them to take
#           the poll.

lenguajes = {
    "aleja": "excel",
    "andrés": "java",
    "edwin": "python",
    "july": "dart",
    "jero": "kotlin",
}

encuestados = ["kelly", "aleja", "andrea", "paola", "juan", "andrés", "edwin"]

for nombres in encuestados:
    if nombres in lenguajes.keys():
        lenguaje_favorito = lenguajes[nombres].title()
        print(f'Hola {nombres.title()}, por lo visto tu lenguaje favorito es {lenguaje_favorito.title()},'
              f' gracias por responder la encuesta')
    else:
        print(f'Hola {nombres.title()}, aun no tomas la encuesta, te invitamos a que lo hagas')






