# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("Mis comidas favoritas son: ")

for food in my_foods:
    print(food)

print("\nLas comidas favoritas de mis amigos son: ")
for food in friend_foods:
    print(food)
