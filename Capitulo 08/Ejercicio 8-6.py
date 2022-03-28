# 8-6. City Names:
#       Write a function called city_country() that takes in the name
#       of a city and its country. The function should return a string formatted like this:
#       "Santiago, Chile"
#       Call your function with at least three city-country pairs, and print the
#       values that are returned.

def ciudad_pais(ciudad, pais):
    completo = f"ciudad: {ciudad}, se encuentra en: {pais}"
    return completo

ciudad_pais_completo = ciudad_pais("ottawa", "canadá")
print(ciudad_pais_completo.title())

ciudad_pais_completo = ciudad_pais("ibagué", "colombia")
print(ciudad_pais_completo.title())

ciudad_pais_completo = ciudad_pais("santiago", "chile")
print(ciudad_pais_completo.title())
