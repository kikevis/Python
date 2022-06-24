#Level 2
""" Escriba un programa que calcule el monto neto de una cuenta bancaria en
función de un registro de transacciones de la entrada de la consola.
El formato del registro de transacciones se muestra a continuación:
D 100
W 200

D significa depósito, mientras que W significa retiro.
Supongamos que se proporciona la siguiente entrada al programa:
D 300
D 300
W 200
D 100
Entonces, la salida debería ser:
500

Sugerencias:
En caso de que se proporcionen datos de entrada a la pregunta,
se debe suponer que se trata de una entrada de consola. """

#solution
netAmount = 0
while True:
    transaction = input()
    if not transaction:
        break
    values = transaction.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        netAmount += amount
    elif operation == "W":
        netAmount -= amount
    else:
        pass
print(netAmount)

#Geovanny E. Villa Sánchez
#KikeViS