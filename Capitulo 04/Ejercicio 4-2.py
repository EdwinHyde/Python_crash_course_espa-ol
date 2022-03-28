# 4-2. Animals: Think of at least three different animals that have a common characteristic.
        # Store the names of these animals in a list, and then use a for loop to
        # print out the name of each animal.

pajaros = ['canario', 'jilguero', 'turpial']
for pajaro in pajaros:
    print(pajaro.upper())

 # •	 Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
for pajaro in pajaros:
    print(f'Me encanta muchísimo el cantar del {pajaro.title()}')

# •	 Add a line at the end of your program stating what these animals have in common.
# You could print a sentence such as Any of these animals would make a great pet!
print("\nEl canto de estas aves es espectacular...")