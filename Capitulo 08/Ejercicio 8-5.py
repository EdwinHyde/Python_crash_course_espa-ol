# 8-5. Cities:
#       Write a function called describe_city() that accepts the name of
#       a city and its country. The function should print a simple sentence, such as
#       Reykjavik is in Iceland. Give the parameter for the country a default value.
#       Call your function for three different cities, at least one of which is not in the
#       default country.

def describe_city(ciudad, pais="Colombia"): #  parametro pais esta "por defecto"
    print(f"{ciudad.title()} se encuentra en {pais}")

describe_city("ibagué") #  se entrega el argumento que se guardará en ciudad
describe_city("manizales") #  se entrega el argumento que se guardará en ciudad
describe_city("cuzco", pais="Perú") #  Se cambian los argumentos porque la ciudad está en otro país



