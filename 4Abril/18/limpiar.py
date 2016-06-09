#!/usr/bin/env python3

#3 Hacer una funcion limpiar que reciba una frase y devuelva esa frase
#sin espacios

frase=str(input("Ingrese frase: "))

def limpiar (frase):
    copia=""
    for a in frase:
        if (a!=' '):
            copia+=a
    print (copia)

limpiar (frase)
