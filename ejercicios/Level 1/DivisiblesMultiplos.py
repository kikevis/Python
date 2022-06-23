#Level 1
""" Pregunta:
Escriba un programa que encuentre todos los números que son divisibles por 7 pero que no son múltiplos de 5, entre 2000 y 3200 (ambos incluidos).
Los números obtenidos deben imprimirse en una secuencia separada por comas en una sola línea.

Sugerencias:
Considere usar el método range(#begin, #end) """

#solution
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i)) #agregar un elemento al final de la lista

print(','.join(l))

#Geovanny E. Villa Sánchez
#KikeViS