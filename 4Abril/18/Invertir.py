#!/usr/bin/env python3

#5 Hacer una funcion reversa que reciba un string y lo devuelva invertido

frase=str(input("Ingrese frase: "))

def Invertir (frase):
    b=0
    copia=""
    for a in range(len(frase),0,-1):    
        copia+=frase[a-1]
    print (copia)

Invertir (frase)

##Otra forma mas sencilla de invertir la frase
##
##def Invertir (frase):
##    print(frase[::-1])
