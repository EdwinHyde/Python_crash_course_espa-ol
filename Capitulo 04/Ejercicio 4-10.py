# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
#   •	 Print the message The first three items in the list are:. Then use a slice to
#       print the first three items from that program’s list.

familia = ['aleja', 'gentil', 'luis', 'andres', 'jeronimo', 'edwin', 'gabriella', 'chavela','antonio']
print(f'Los 3 primeros miembros en esta lista son: {familia[:3]}')

#   •	 Print the message Three items from the middle of the list are:. Use a slice to
#       print three items from the middle of the list.

print(f'Los 3 miembros de en medio en esta lista son: {familia[3:6]}')

#   •	 Print the message The last three items in the list are:. Use a slice to print the
#       last three items in the list.

print(f'Finalmente, los 3 miembros al final de esta lista son: {familia[6:]}')


