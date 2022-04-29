def conversor(tipo_pesos, valor_usd):
    pesos = float(input("¿Cuantos pesos " + tipo_pesos + " tienes?: "))
    usd = pesos / valor_usd
    usd = round(usd, 2)
    usd = str(usd)
    print("Tienes $" + usd + " dolares.")

menu = """
Bienvenidos al conversor de manedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion:
"""
opcion = int(input(menu))

if opcion == 1:
    #COP (valor fijo)
    conversor("Colombianos", 3800)
elif opcion == 2:
    #ARG (valor fijo)
    conversor("Argentinos", 60)
elif opcion == 3:
    #MEX (valor fijo)
    conversor("Mexicanos", 25)
else:
    print("Ingresa una opcion correcta")

#Geovanny E. Villa Sánchez
#hola
#COP (valor fijo)