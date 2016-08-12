#!/usr/bin/env python3

#5 Hacer una función que devuelva una lista de C números aleatorios entre
#N1 y N2 //def crearLista( 6, 2, 8) -> [2, 4, 4, 6, 7, 7]

import random

c=int(input("Ingrese largo de lista: "))
n1=int(input("Ingrese minimo: "))
n2=int(input("Ingrese maximo: "))

def CrearLista(c,n1,n2):
    lista=[]
    for i in range (c):
        lista.append(random.randrange(n1,n2))
    return sorted(lista)

CrearLista(c,n1,n2)
