#Level 2
""" Escriba un programa que calcule el valor de a + aa + aaa + aaaa con un
dígito dado como el valor de a.
Supongamos que se proporciona la siguiente entrada al programa:
9
Entonces, la salida debería ser:
11106

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta, se debe
suponer que se trata de una entrada de consola. """

#solution
a = input()
n1 = int ("%s" % a)
n2 = int ("%s%s" % (a,a))
n3 = int ("%s%s%s" % (a,a,a))
n4 = int ("%s%s%s%s" % (a,a,a,a))
print (n1+n2+n3+n4)

#Geovanny E. Villa Sánchez
#KikeViS