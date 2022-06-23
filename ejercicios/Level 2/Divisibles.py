#Level 2
""" Escriba un programa que acepte una secuencia de números binarios de 4 dígitos
separados por comas como su entrada y luego verifique si son divisibles por 5 o no.
Los números que son divisibles por 5 se deben imprimir en una secuencia separada por
comas.
Ejemplo:
0100,0011,1010,1001
Entonces la salida debería ser:
1010
Notas: suponga que la consola ingresa los datos.

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que
se trata de una entrada de consola. """

#solution
value = []
items = [x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp % 5:
        value.append(p)

print(','.join(value))

#Geovanny E. Villa Sánchez
#KikeViS