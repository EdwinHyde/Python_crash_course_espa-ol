# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
#       stage of life. Set a value for the variable age, and then:
#           •	 If the person is less than 2 years old, print a message that the person is
#               a baby.
#           •	 If the person is at least 2 years old but less than 4, print a message that
#               the person is a toddler.
#           •	 If the person is at least 4 years old but less than 13, print a message that
#               the person is a kid.
#           •	 If the person is at least 13 years old but less than 20, print a message that
#               the person is a teenager.
#           •	 If the person is at least 20 years old but less than 65, print a message that
#               the person is an adult.
#           •	 If the person is age 65 or older, print a message that the person is an
#               elder.

edad = 100
if edad < 2:
    print("Esta persona es un bebé")
elif edad < 4:
    print("Esta persona es un niño pequeño")
elif edad < 13:
    print("Esta persona es un niño")
elif edad < 20:
    print("Esta persona es un adolescente")
elif edad < 65:
    print("Esta persona es un adulto")
else:
    edad >= 65
    print("Esta persona es un anciano")