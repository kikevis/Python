""" Escriba un programa que pueda calcular el factorial de un número dado.
Los resultados deben imprimirse en una secuencia separada por comas en una sola línea.
Supongamos que se proporciona la siguiente entrada al programa:
8
Entonces, la salida debería ser:
40320

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola. """

#solution
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))

#Geovanny E. Villa Sánchez
#KikeVis