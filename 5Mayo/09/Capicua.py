#!/usr/bin/env python3

#3 Hacer una funcion que devuelva True un string S, que recibe como parámetro,
#es palíndroma (capicua).

S=(input("Ingrese palabra: "))

def Capicua(S):
    auxS=S[::-1]
    for i in range(len(S)):
        if auxS[i]!=S[i]:
            return False
    return True

Capicua (S)
