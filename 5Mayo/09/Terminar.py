#!/usr/bin/env python3

#2 Hacer una funcion que recibe S1 y S2 y devuelve True si S1 termina con S2, o
#S2 termina en S1, sino devuelve False
#Maysuculas y minusculas se consideran iguales

S1=(input("Ingrese palabra S1: "))
S2=(input("Ingrese palabra S2: "))

def Terminar (S1,S2):
    auxS1=S1.lower()
    auxS2=S2.lower()
    if (auxS1 in auxS2 or auxS2 in auxS1):
        if ((auxS1[-1]==S2[-1]) or (auxS2[-1]==S1[-1])):
            return True
        else:
            return False
    else:
        return False

Terminar (S1,S2)
