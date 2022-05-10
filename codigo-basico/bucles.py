#def run(num, rept):
#    if num <= rept:
#        cont = num
#        print(str(2 ** cont))
#        run(num+1, rept)
#    else:
#        print("Fin!")
#
#if __name__ == "__main__":
#    repeticiones = int(input("Cuantas potencias: "))
#    run(0, repeticiones)


#def potencia(numero):
#    potencia = 1
#    while (potencia <= 10):
#        result = numero ** potencia
#        print('Potencia de {} elevado a la {} es {}'.format(numero, potencia, result))
#        potencia += 1
#
#
#def run():
#    numero = int(input('Escribe el numero al cual quieres averiguarle la potencia: '))
#    potencia(numero)
#
#if __name__ == "__main__":
#    run()


def run():
    print("ELEVAR NUMERO BASE A N POTENCIAS LIMITE DE RESULTADO 1000")
    LIMITE = 1000
    base = int(input('Ingrese numero base: '))

    contador = 0
    resultado = base**contador

    while resultado < LIMITE:
        print('{} elevado a la {} es: {}'.format(base,contador,resultado))
        contador+=1
        resultado = base**contador

if __name__ == '__main__':
    run()