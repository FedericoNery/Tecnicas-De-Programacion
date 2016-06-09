#!/usr/bin/env python3

#6 Programar una funcion que reciba 2 strings y devuelva la que tenga
#mayor longitud

s=(str(input("Ingrese frase: ")))
t=(str(input("Ingrese frase: ")))

def MasLong(s,t):
    if (len(s)>len(t)):
        print(s)
    elif (len(s)<len(t)):
        print(t)
    else:
        print ("Ambos strings tienen la misma longitud")

MasLong(s,t)
