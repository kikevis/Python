""" Escriba un programa que acepte una secuencia de números separados por comas desde la consola y genere una lista y una tupla que contenga cada número.
Supongamos que se proporciona la siguiente entrada al programa:
34,67,55,33,12,98
Entonces, la salida debería ser:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola.
El método tuple () puede convertir la lista en tupla """

#solution
values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)