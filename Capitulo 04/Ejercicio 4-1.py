# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
pizza_sabores = ['piña', 'pepperoni', 'hawaiana']

for pizza in pizza_sabores:
    print(pizza)

#   •	 Modify your for loop to print a sentence using the name of the pizza
#       instead of printing just the name of the pizza. For each pizza you should
#       have one line of output containing a simple statement like I like pepperoni pizza.

for pizza in pizza_sabores:
    print(f'La verdad es que no me gusta mucho la pizza con sabor a {pizza}')

#   •	 Add a line at the end of your program, outside the for loop, that states
#       how much you like pizza. The output should consist of three or more lines
#       about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

for pizza in pizza_sabores:
    print(f'Bueno, siendo sinceros no me gusta para nada la pizza, ni siquiera la que tiene sabor a {pizza.title()}')
print('Creo que no me gusta la pizza...')

