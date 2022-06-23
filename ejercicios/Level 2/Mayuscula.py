#Level 2
""" Escriba un programa que acepte una secuencia de líneas como entrada e imprima las líneas después de poner todos los caracteres de la oración en mayúscula.
Supongamos que se proporciona la siguiente entrada al programa:
Hola Mundo
La práctica hace la perfección
Entonces, la salida debería ser:
HOLA MUNDO
LA PRÁCTICA HACE LA PERFECCIÓN

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola. """

#solution
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)

#Geovanny E. Villa Sánchez
#KikeViS