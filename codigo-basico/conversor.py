menu = """
Bienvenidos al conversor de manedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion:
"""
opcion = int(input(menu))

if opcion == 1:
    #COP a USD (valor fijo)
    cop = float(input("¿Cuantos pesos colombianos tienes?: "))
    valor_usd = 3742.67
    usd = cop / valor_usd
    usd = round(usd, 2)
    usd = str(usd)
    print("Tienes $" + usd + " dolares.")
elif opcion == 2:
    #ARG a USD (valor fijo)
    arg = float(input("¿Cuantos pesos argentinos tienes?: "))
    valor_usd = 112.53
    usd = arg / valor_usd
    usd = round(usd, 2)
    usd = str(usd)
    print("Tienes $" + usd + " dolares.")
elif opcion == 3:
    #MEX a USD (valor fijo)
    mex = float(input("¿Cuantos pesos mexicanos tienes?: "))
    valor_usd = 19.94
    usd = mex / valor_usd
    usd = round(usd, 2)
    usd = str(usd)
    print("Tienes $" + usd + " dolares.")
else:
    print("Ingresa una opcion correcta")

#COP a USD (valor fijo)
#cop = float(input("¿Cuantos pesos colombianos tienes?: "))
#valor_usd = 3742.67
#usd = cop / valor_usd
#usd = round(usd, 2)
#usd = str(usd)
#print("Tienes $" + usd + " dolares.")

#USD a COP (valor fijo)
#usd = float(input("¿Cuantos dolares estadounidenses tienes?: "))
#valor_cop = 0.0002671889
#cop = usd / valor_cop
#cop = round(cop, 6)
#cop = str(cop)
#print("Tienes $" + cop + " COP.")

#hola