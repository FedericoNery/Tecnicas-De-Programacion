#!/usr/bin/env python3

#9 Hacer una función que reciba como parámetros N1 y N2 y devuelva cuántos
#múltiplos de N1 hay que sean menores que N2
#mulMenores(2, 15) -> 6    (4,6, 8, 10, 12, 14)
#hacerlo con for y con while ¿Cuá es la ventaja de cada una?

N1=int(input("Ingrese numero menor: "))
N2=int(input("Ingrese numero mayor: "))

def Multiplos (N1,N2):
    aux=cantidad=0
    for i in range (N1+N1,N2+1,N1):
        print(i)
        cantidad+=1
    print("-----")
    return cantidad

Multiplos (N1,N2)
