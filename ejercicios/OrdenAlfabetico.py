#Level 2
""" Escriba un programa que acepte una secuencia de palabras separadas por comas como entrada e imprima las palabras en una secuencia separada por comas después de ordenarlas alfabéticamente.
Supongamos que se proporciona la siguiente entrada al programa:
sin,hola,bolso,mundo
Entonces, la salida debería ser:
bolsa hola sin mundo

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola. """

#solution
items=[x for x in input().split(',')]
items.sort()
print(','.join(items))

#Geovanny E. Villa Sánchez
#KikeViS