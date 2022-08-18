#Level 3
""" Debe escribir un programa para clasificar las tuplas (nombre, edad, altura) en orden
ascendente, donde el nombre es una cadena, la edad y la altura son números. Las tuplas son
ingresadas por consola. El criterio de clasificación es:
1: Ordenar según el nombre;
2: Luego ordene según la edad;
3: Luego ordenar por puntuación.
La prioridad es ese nombre > edad > puntuación.
Si se dan las siguientes tuplas como entrada al programa:
Tomás, 19, 80
Juan,20,90
Juan, 17, 91
Juan, 17, 93
Json,21,85
Entonces, la salida del programa debe ser:
[('Juan', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21 ', '85'),
('Tom', '19', '80')]

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata
de una entrada de consola.
Usamos itemgetter para habilitar varias claves de ordenación."""

#solution
from operator import itemgetter, attrgetter

l = []
while True:
    s = raw_input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print sorted(l, key=itemgetter(0,1,2))

#Geovanny E. Villa Sánchez
#KikeViS