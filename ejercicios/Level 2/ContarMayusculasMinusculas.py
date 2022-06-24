#Level 2
""" Escriba un programa que acepte una oración y calcule el número de letras
mayúsculas y minúsculas.
Supongamos que se proporciona la siguiente entrada al programa:
¡Hola Mundo!
Entonces, la salida debería ser:
MAYÚSCULAS 1
MINUSCULAS 9

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se
trata de una entrada de consola. """

#solucion
s = input()
d = {"UPPER CASE": 0, "LOWER CASE": 0}
for c in s:
    if c.isupper():
        d["UPPER CASE"] += 1
    elif c.islower():
        d["LOWER CASE"] += 1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])

#Geovanny E. Villa Sánchez
#KikeViS