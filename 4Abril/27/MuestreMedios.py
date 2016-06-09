#!/usr/bin/env python3

#Escriba una funcion que reciba una lista y que devuelve otra que muestre
#los medios (elimine extremos)

lista = [1,2,3,4,5,6]

def medios(lista):
    nuevalista=lista.copy()
    nuevalista.pop(0)
    nuevalista.pop(len(lista)-2)
    print (nuevalista)

medios(lista)

