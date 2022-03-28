# 6-5. Rivers: Make a dictionary containing three major rivers and the country
#       each river runs through. One key-value pair might be 'nile': 'egypt'.
#           •	 Use a loop to print a sentence about each river, such as The Nile runs
#               through Egypt.
#           •	 Use a loop to print the name of each river included in the dictionary.
#           •	 Use a loop to print the name of each country included in the dictionary.

rios = {
    'nilo': 'Egipto',
    'amazonas': 'suramerica',
    'yangtsé': 'china'
    }

for rio, pais in rios.items():
    print(f'El rio {rio.title()} se encuentra ubicado en {pais.title()}')
print("")

for rio in rios.keys():
    print(rio.title())
print("")
for pais in rios.values():
    print(pais.title())



