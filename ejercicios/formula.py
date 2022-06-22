""" Escriba un programa que calcule e imprima el valor de acuerdo con la fórmula dada:
Q = raíz cuadrada de [(2 * C * D)/H]
Los siguientes son los valores fijos de C y H:
C es 50. H es 30.
D es la variable cuyos valores deben ingresarse en su programa en una secuencia separada por comas.
Ejemplo
Supongamos que se le da al programa la siguiente secuencia de entrada separada por comas:
100,150,180
La salida del programa debe ser:
18,22,24

Sugerencias:
Si el resultado recibido está en formato decimal, debe redondearse al valor más cercano (por ejemplo, si el resultado recibido es 26,0, debe imprimirse como 26)
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola. """

#solution
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))

#Geovanny E. Villa Sánchez
#KikeViS