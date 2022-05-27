# 10-10. Common Words:
# Visit Project Gutenberg (https://gutenberg.org/) and find a few texts you’d like to analyze.
# Download the text files for these works, or copy the raw text from your browser into a text file on your computer.
# You can use the count() method to find out how many times a word or phrase appears in a string.
# For example, the following code counts the number of times 'row' appears in a string:
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for,
# regardless of how it’s formatted.
# Write a program that reads the files you found at Project Gutenberg and determines how many times
# the word 'the' appears in each text.
# This will be an approximation because it will also count words such as 'then' and 'there'.
# Try counting 'the ', with a space in the string, and see how much lower your count is.

def contar_palabras(libros):

    buscar_palabra = input('Escriba la palabra que desea buscar: ')
    for libro in libros:
        with open(libro, encoding='utf-8') as f:
            contenido = f.read()

            print(f"La palabra '{buscar_palabra}' se encuentra {contenido.count(buscar_palabra)} veces en el libro {libro}")
            print(f"La palabra '{buscar_palabra}' se encuentra {contenido.lower().count(buscar_palabra)} "
                  f"veces en el libro {libro}")

libros = ['jekyll.txt', 'odisea.txt']
contar_palabras(libros)