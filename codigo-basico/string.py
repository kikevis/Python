name = """
Bienvenido, ingresa un nombre
"""
nombre = str(input(name))

#STRIP es un metodo que eimina los espacios basura que estan al principio o al final
nombre = nombre.replace(' ', '').strip()

option = """
Bienvenido

1 - MAYUSCULA
2 - MINISCULA
3 - PRIMERA MAYUSCULA

Elige una opcion:
"""

opcion = int(input(option))

if opcion == 1:
    #UPPER combierte el texto a mayuscula
    print(nombre.upper())
elif opcion == 2:
    #LOWER combierte el texto a miniscula
    print(nombre.lower())
elif opcion == 3:
    #CAPITALIZE combiarte el texto a la primera letra en mayuscula
    print(nombre.capitalize())
else:
    print("Ingresa una opcion correcta")


letters = """
Hola de nuevo

¿Te gustaria saber cuantas letras tiene tu nombre?

1 - SI
2 - NO

Elige una opcion:
"""

letras = int(input(letters))

if letras == 1:
    #LEN te dice el numero de caractares en una variable
    num = str(len(nombre))
    print("El nombre tiene {} caracteres".format(num))
elif letras == 2:
    print("Ok, Bye")
else:
    print("Ingresa una opcion correcta")

#Geovanny E. Villa Sánchez