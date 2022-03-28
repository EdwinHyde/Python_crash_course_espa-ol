# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
#           the sandwich 'pastrami' appears in the list at least three times.
#           Add code near the beginning of your program to print a message saying the deli has
#           run out of pastrami, and then use a while loop to remove all occurrences of
#           'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
#           in finished_sandwiches.

sandwich_orders = ["pastrami", "queso", "jamon", "pastrami", "huevo", "verduras", "pastrami"]
finished_sandwiches = []
print("Para el dia de hoy te ofrecemos el siguiente menú: ")
for sandwich in sandwich_orders:
    print(f"Sandwich de: {sandwich.title()}")

print("\nLamentamos informar que se nos ha acabado el pastrami. ")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Te he preparado un sandwich de {sandwich.title()}")
    finished_sandwiches.append(sandwich.title())

print("\nComo se ha acabado el sandwich de pastrami, están listos los siguientes sandwiches: ")
for sandwich in sorted(finished_sandwiches):
    print(sandwich)



