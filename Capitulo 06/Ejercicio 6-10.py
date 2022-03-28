# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
#           so each person can have more than one favorite number.
#           Then print each person’s name along with their favorite numbers.

numeros_favoritos = {
    "juliana": [2, 4, 6, 8],
    "eider": [3, 6, 9, 12],
    "Alex": [4, 8, 12, 16],
    "Darwin": [5, 10, 15, 20],
    "natalia": [10, 20, 30, 40],
    }

for nombre, numeros in numeros_favoritos.items():
    print(f"Los números favoritos de {nombre.title()} son: ")
    for numero in numeros:
        print(f'\t{numero}')
    print("")