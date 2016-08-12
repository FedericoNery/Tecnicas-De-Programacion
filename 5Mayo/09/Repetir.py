#!/usr/bin/env python3

#1 Hacer una funcion que reciba un string S y un numero N, tiene que devolver
# un string formado repitiendo las N primeras letras de S, luego las N-1,
#las N-2, etc...

S=(input("Ingrese palabra: "))
N=int(input("Ingrese numero: "))

def Repetir (S,N):
    nuevoS=" "
    for i in range (N):
        nuevoS=nuevoS+S[:N-i]    
    return nuevoS

Repetir (S,N)
