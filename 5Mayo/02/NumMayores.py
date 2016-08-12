#!/usr/bin/env python3

#Dada una lista de numeros enteros y un numero n generar otra lista (y mostrarla)
#con todos los numeros de la lista que sean mayores a n

numeros = [10,20,30,40,50,60]
n = 45

def NumMayores(numeros,n):
    nuevalista = [for item in numeros if (numero>n)]
    print (nuevalista)

NumMayores(numeros,n)
