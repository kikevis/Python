#Level 2
""" Escriba un programa que acepte una oración y calcule el número de letras y dígitos.
Supongamos que se proporciona la siguiente entrada al programa:
¡Hola Mundo! 123
Entonces, la salida debería ser:
LETRAS 10
DIGITOS 3

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se
trata de una entrada de consola. """

#solution
s = input()
d = {"DIGITS": 0, "LETTERS": 0}
for c in s:
    if c.isdigit():
        d["DIGITS"] += 1
    elif c.isalpha():
        d["LETTERS"] += 1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])

#Geovanny E. Villa Sánchez
#KikeViS