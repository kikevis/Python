#Level 2
""" Escriba un programa que acepte una secuencia de líneas como entrada e imprima las líneas después de poner la primera letra de los caracteres de la oración en mayuscula.
Supongamos que se proporciona la siguiente entrada al programa:
HOLA MUNDO
Entonces, la salida debería ser:
Hola mundo

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola. """

#solution
lines = []
while True:
    s = input()
    if s:
        lines.append(s.capitalize())
    else:
        break;

for sentence in lines:
    print(sentence)

#Geovanny E. Villa Sánchez
#KikeViS