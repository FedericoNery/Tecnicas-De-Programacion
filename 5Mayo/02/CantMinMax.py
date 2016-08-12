#!/usr/bin/env python3

#Crear una funcion que reciba: - C cantidad, - m min - M max
#y devuelva una lista ordenada de C numeros aleatorios entre m y M

import random

cantidad=10
minimo=1
maximo=100

def CantMinMax(cantidad,minimo,maximo):
    lista=[]
    for i in range (1,cantidad+1):
        numero = random.randrange(minimo,maximo)
        lista.append(numero)
    print (sorted(lista))

CantMinMax(cantidad,minimo,maximo)
