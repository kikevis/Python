name = """
Bienvenido, ingresa un nombre
"""
nombre = str(input(name))

#STRIP es un metodo que eimina los espacios basura que estan al principio o al final
nombre = nombre.strip()

option = """
Bienvenido

1 - MAYUSCULA
2 - MINISCULA
3 - PRIMERA MAYUSCULA
4 - REMPLAZAR ALGUNA LETRA DEL NOMBRE

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
elif opcion == 4:
    
else:
    print("Ingresa una opcion correcta")

#Geovanny E. Villa Sánchez