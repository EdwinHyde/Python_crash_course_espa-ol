# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
#       •	 If the alien is green, print a message that the player earned 5 points.
#       •	 If the alien is yellow, print a message that the player earned 10 points.
#       •	 If the alien is red, print a message that the player earned 15 points.
#       •	 Write three versions of this program, making sure each message is printed
#               for the appropriate color alien.

alien_color = "Verde"
if alien_color == "Verde":
    print("Haz ganado 5 puntos")
elif alien_color == "Amarillo":
    print("Haz ganado 10 puntos")
else:
    print("Has ganado 15 puntos")

alien_color = "Amarillo"
if alien_color == "Verde":
    print("Haz ganado 5 puntos")
elif alien_color == "Amarillo":
    print("Haz ganado 10 puntos")
else:
    print("Has ganado 15 puntos")

alien_color = "Azul"
if alien_color == "Verde":
    print("Haz ganado 5 puntos")
elif alien_color == "Amarillo":
    print("Haz ganado 10 puntos")
else:
    print("Has ganado 15 puntos")