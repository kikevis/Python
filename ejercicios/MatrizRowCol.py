#Level 1
""" Escriba un programa que tome 2 dígitos, X, Y como entrada y genere una matriz bidimensional. El valor del elemento en la i-ésima fila y la j-ésima columna de la matriz debe ser i*j.
Nota: i=0,1.., X-1; j=0,1,¡Y-1.
Ejemplo
Supongamos que se le dan las siguientes entradas al programa:
3,5
Entonces, la salida del programa debe ser:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Sugerencias:
Nota: En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola separada por comas. """

#solution
input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist)

#Geovanny E. Villa Sánchez
#KikeViS