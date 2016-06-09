#!/usr/bin/env python3

#Escriba una funcion llamada esta_ordenada que tome una lista como parametro
#y retorne True si la lista esta ordenada de forma ascendente o False si no lo
#esta. Usted puede asumir como precondicion que los elementos son comparables
# con los operadores relacionales.
#esta_ordenada([1,2,2]) debe retornar True
#esta_ordenada(['b','a']) debe retornar False.

lista = [1,2,3,4]
lista1 = [1,3,2,4]
lista2 = ["a","b","c","d"]
lista3 = ["a","b","d","c"]

def EstaOrdenada (lista):
    itemant=lista[0]
    for item in lista:
        itemact=item
        if (itemant>itemact):
            return False
        else:
            pass
        itemant=item
    return True

EstaOrdenada(lista)
