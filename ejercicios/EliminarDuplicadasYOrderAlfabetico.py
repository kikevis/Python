#Level 2
""" Escriba un programa que acepte una secuencia de palabras separadas
por espacios en blanco como entrada e imprima las palabras después de eliminar
todas las palabras duplicadas y ordenarlas alfanuméricamente.
Supongamos que se proporciona la siguiente entrada al programa:
hola mundo y la práctica hace la perfección y hola mundo otra vez
Entonces, la salida debería ser:
de nuevo y hola hace el mundo de práctica perfecto

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer
que se trata de una entrada de consola.
Usamos set container para eliminar datos duplicados automáticamente y luego
usamos sorted() para ordenar los datos. """

#solution

s = input()
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))