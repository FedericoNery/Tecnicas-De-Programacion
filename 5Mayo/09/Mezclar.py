#!/usr/bin/env python3

#4 Hacer una función que recibe S1 y S2 (dos strings) y devuelve un string S
#formada por la primer letra de S1, la primer letra de S2, la segunda de S1,
#la segunda de S2 etc.
#mezclar(“uno”, “dos”) -> udnoos
#mezclar(“abcd”, “mnopqr”) -> ambncodpqr

S1=(input("Ingrese palabra S1: "))
S2=(input("Ingrese palabra S2: "))

def Mezclar(S1,S2):
    nuevoS=" "
    if len(S1)>len(S2):
        largo=len(S1)
    else:
        largo=len(S2)
    for i in range(largo):
        if i<len(S1):            
            nuevoS+=S1[i]
        if i<len(S2):
            nuevoS+=S2[i]
    return nuevoS

Mezclar(S1,S2)
