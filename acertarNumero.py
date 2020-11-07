# Programa para jugar a acertar un múmero que se genera
# aleatoriamente entre 9 y 99 ambos inclusive

import sys
import random


def pedir_numero(texto):
    numero = input(texto)
    return numero


def pedir_numero_intervalo(texto, minimo, maximo):
    texto_llamada = texto + " entre " + str(minimo) + " y " + str(maximo) + " : "
    numero = pedir_numero(texto_llamada)
    return numero


def jugar():
    MIN = 0
    MAX = 100

    numero = pedir_numero_intervalo("Dime un número ", MIN, MAX)

    print(numero)
    return


jugar()
