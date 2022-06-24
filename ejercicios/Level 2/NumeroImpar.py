#Level 2
""" Escriba un programa que encuentre todos los números entre 1000 y 3000
(ambos incluidos) de modo que cada dígito del número sea un número par.
Los números obtenidos deben imprimirse en una secuencia separada por comas
en una sola línea.

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer
que se trata de una entrada de consola. """

#solution
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0]) % 2 != 0) and (int(s[1]) % 2 != 0) and (int(s[2]) % 2 != 0) and (int(s[3]) % 2 != 0):
        values.append(s)
print(', '.join(values))

#Geovanny E. Villa Sánchez
#KikeViS