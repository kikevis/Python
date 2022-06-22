""" Defina una clase que tenga al menos dos métodos:
getString: para obtener una cadena de la entrada de la consola
printString: para imprimir la cadena en mayúsculas.
También incluya una función de prueba simple para probar los métodos de clase.

Sugerencias:
Use el método __init__ para construir algunos parámetros """

#solution
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()