# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cubos = []
for value in range(1,11):
    cubo = value**3
    cubos.append(cubo)
    print(f'El cubo de {value} es: {cubo}')
print(f'Y todos los cubos reunidos son: {cubos}')
print("Reto superado")

#OTRA FORMA DE RESOLVER EL EJERICICIO
cubos = [print(f'El cubo de {cubo} es {cubo**3}') for cubo in range(1,11)]
print("Soy un duro... :)")



