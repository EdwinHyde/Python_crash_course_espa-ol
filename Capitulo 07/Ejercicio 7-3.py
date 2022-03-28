# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
#       number is a multiple of 10 or not.

number = input("Please, write a number: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is multiple of 10")
else:
    print(f"\nThe number {number} isn't multiple of 10. ")
