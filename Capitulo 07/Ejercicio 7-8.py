# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.
#       Then make an empty list called finished_sandwiches.
#       Loop through the list of sandwich orders and print a message for each order, such
#       as I made your tuna sandwich.
#       As each sandwich is made, move it to the list of finished sandwiches.
#       After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ["queso", "jamon", "huevo", "verduras"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Te he preparado un sandwich de {sandwich.title()}")
    finished_sandwiches.append(sandwich.title())

print("\nA continuacion se muestran los sandwiches finalizados: ")
for sandwich in sorted(finished_sandwiches):
    print(sandwich)