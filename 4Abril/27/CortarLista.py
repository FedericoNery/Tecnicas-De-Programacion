#!/usr/bin/env python3

#Escriba una funcion llamada cortar que reciba una lista y la modifique
#eliminando el primero y el ultimo elemento retornando None

def cortar(lista):
    lista.pop(0)
    lista.pop(len(lista)-1)

cortar(lista)
