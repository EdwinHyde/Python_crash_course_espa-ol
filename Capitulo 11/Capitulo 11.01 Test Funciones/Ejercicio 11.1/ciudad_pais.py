# 11-1. City, Country:
# Write a function that accepts two parameters: a city name and a country name.
# The function should return a single string of the form City, Country, such as Santiago, Chile.
# Store the function in a module called city_functions.py.

def ciudad_pais(ciudad, pais):
    pais_completo = f"{ciudad} {pais}"
    return pais_completo.title()