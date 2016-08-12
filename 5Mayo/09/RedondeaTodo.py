#!/usr/bin/env python3

#7 Usar la función del punto anterior en una función que recibe una lista de
#números decimales y devuelve una lista con todos sus números redondeados a 1
#decimal. //redondeaTodo( [1.55, 5, 2.69, 0.258]) -> [1.6, 5, 2.7, 0.3]

lista=[1.55, 5, 2.69, 0.258]

def Redondear(F,D):
    F=round(F,D)
    return F

def RedondeaTodo(lista):
    nuevalista=[]
    for item in lista:
        item=Redondear(item,1)
        nuevalista.append(item)
    return nuevalista

RedondeaTodo(lista)                     
