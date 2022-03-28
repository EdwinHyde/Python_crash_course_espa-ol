# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

# multiplos = []
# for value in range(1,31):
#     if value%3 == 0:
#         multiplo = value
#         print(multiplo)
#         multiplos.append(multiplo)
# print(f'Los multiplos de 3 son: {multiplos}')
# print("Resuelto")

multiplos = [print(value) for value in range(1,31) if value%3 == 0]
