#Level 2
""" Usa una lista de comprensión para elevar al cuadrado cada número impar en una
lista. La lista se ingresa mediante una secuencia de números separados por comas.
Supongamos que se proporciona la siguiente entrada al programa:
1,2,3,4,5,6,7,8,9
Entonces, la salida debería ser:
1,3,5,7,9

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer
que se trata de una entrada de consola. """

#solution
values = input()
numbers = [int(x) for x in values.split(",") if int(x) % 2 != 0]
print(",".join(str(x) for x in numbers))

#Geovanny E. Villa Sánchez
#KikeViS