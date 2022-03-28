# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
#       create to ten. If you want to try more comparisons, write more tests and add
#       them to conditional_tests.py. Have at least one True and one False result for
#       each of the following:
#           •	 Tests for equality and inequality with strings
#           •	 Tests using the lower() method
#           •	 Numerical tests involving equality and inequality, greater than and
#                less than, greater than or equal to, and less than or equal to
#           •	 Tests using the and keyword and the or keyword
#           •	 Test whether an item is in a list
#           •	 Test whether an item is not in a list

familia = ["edwin", "alejandra", "chavela", "gentil", "andrés"]
programador = "Edwin"
print(familia[0] != familia[1])
print(familia[0] == programador.lower())

numeros = [10, 50, 100, 10, 45, 90]
if numeros[0] >= numeros[4]:
    print(f'El número {numeros[0]} es mayor que {numeros[4]}')
else:
    print(f'El número {numeros[0]} es menor que {numeros[4]}')

print(10 in numeros)
print("chavela" not in familia)