# Programa para jugar a acertar un múmero que se genera
# aleatoriamente entre 9 y 99 ambos inclusive

import sys
import random


def pedir_entero(texto):
    try:
        numero = int(input(texto))

    except ValueError as e:
        print("Error, no hay valor o no es numérico", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit()

    return numero


def pedir_entero_intervalo(texto, minimo, maximo):
    texto_llamada = texto + " entre " + str(minimo) + " y " + str(maximo) + " : "
    numero = pedir_entero(texto_llamada)
    return numero


def jugar():
    minimo = 0
    maximo = 100
    valorCorrecto = random.randint(minimo, maximo)
    acertado = False
    intentos = 0
    while not acertado:
        intentos = intentos + 1
        numero = pedir_entero_intervalo("Dime un número ", minimo, maximo)
        if numero == valorCorrecto:
            print("Enhorabuena, has acertado en " + str(intentos) + " intentos")
            acertado = True
        elif numero < valorCorrecto:
            minimo = numero
            print("Demasiado pequeño")
        else:
            maximo = numero
            print("Demasiaso grande")

    return


jugar()
