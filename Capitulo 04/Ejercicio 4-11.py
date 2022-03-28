# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#       •	 Add a new pizza to the original list.
#       •	 Add a different pizza to the list friend_pizzas.
#       •	 Prove that you have two separate lists. Print the message My favorite # pizzas are:,
#           and then use a for loop to print the first list.
#           Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.

pizza_sabores = ['piña', 'pepperoni', 'hawaiana']
pizza_amigos = pizza_sabores[:]

pizza_sabores.append('ranchera')
pizza_amigos.append('Paisa')

print('Mis pizzas favoritas son: ')
for pizza in pizza_sabores:
    print(pizza.title())

print('Las pizzas favoritas de mis amigos son: ')
for pizza in pizza_amigos:
    print(pizza.title())