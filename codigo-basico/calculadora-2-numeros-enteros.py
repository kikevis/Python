def suma(a,b):
    sumita = a + b
    return sumita
def resta(a,b):
    restica = a - b
    return restica
def multiplicacion(a,b):
    multi = a * b
    return multi

def division(a,b):
    divi = a / b
    return div

print("""
    Bienvenido a la calculadora de sebas
    1. Si quieres sumar
    2. Si quieres restar
    3. Si quieres multiplicar
    4. Si quieres dividir
""")

respuesta = int(input("DIGITE SU OPCION: "))
numero_a = int(input("Digite El primer numero: "))
numero_b = int(input("Digite el segundo numero: "))

if respuesta == 1:
    resultado = suma(numero_a,numero_b)
    print(resultado)
elif respuesta == 2:
    resultado = resta(numero_a,numero_b)
    print (resultado)
elif respuesta == 3:
    resultado = multiplicacion(numero_a,numero_b)
    print(resultado)
elif respuesta == 4:
    resultado = division(numero_a,numero_b)
    print(resultado)

#Geovanny E. Villa Sánchez