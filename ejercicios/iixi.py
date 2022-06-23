#Level 2
""" Con un número entero n dado, escriba un programa para generar un diccionario que contenga (i, i*i) tal que sea un número entero entre 1 y n (ambos incluidos). y luego el programa debería imprimir el diccionario.
Supongamos que se proporciona la siguiente entrada al programa:
8
Entonces, la salida debería ser:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola.
Considere usar dict() """

#solution
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)

#Geovanny E. Villa Sánchez
#KikeViS