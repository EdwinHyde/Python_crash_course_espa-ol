nombre_de_archivo = "programando.txt"  # Creamos un archivo de texto plano y lo asignamos a la variable.

with open(nombre_de_archivo, 'w') as file_object:  # Se reciben 2 argumentos: el nombre del archivo y el
    # segundo argumento 'w' le dice a python que debe abrir el archivo en modo de escritura.
    # 'r' = modo de lectura
    # 'w' = modo de escritura
    # 'a' = modo Append
    # 'r+' = modo de lectura-escritura.
    # si se omite el argumento del modo el archivo se abre en modo de solo lectura que esta predeterminado.

    file_object.write("Me gusta programar.")  # El metodo write escribe una cadena de texto en el archivo.