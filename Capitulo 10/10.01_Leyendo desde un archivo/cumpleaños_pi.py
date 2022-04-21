# AVERIGUAR SI MI FECHA DE CUMPLEAÑOS SE ENCUENTRA EN EL NUMERO PI

filename = 'archivos_texto/pi_millon_de_digitos.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

cumpleaños = input("Ingrese la fecha de su cumpleaños (mmddaa): ")
if cumpleaños in pi_string:
    print("Tu fecha de cumpleaños aparece en el numero pi!!!")
else:
    print("Tu fecha de cumpleaños no aparece en el numero pi.")


