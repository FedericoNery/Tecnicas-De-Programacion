#!/usr/bin/env python3

#Escriba una funcion que recorra una lista de cadenas imprimiendo la longitud
#de cada una. Que pasa si le pasa un entero a len()?

lista = ["uno","dos","tres","cuatro"]
listaint = [1,2,3,4]
def Recorrer (lista):
    for item in lista:
        print (len(item))

Recorrer (lista)

#Si es una lista de enteros, te dice que el tipo int no tiene longitud
