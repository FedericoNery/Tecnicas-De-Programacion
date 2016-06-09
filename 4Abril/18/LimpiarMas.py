#!/usr/bin/env python3

#4 Igual al 3 pero eliminar, comas, puntos o puntos y coma

frase=str(input("Ingrese frase: "))

def limpiarMas (frase):
    copia=""
    for a in frase:
        if ((a!=' ') and (a!=',') and (a!='.') and (a!=';')):
            copia+=a
    print (copia)

limpiarMas (frase)
