#!/usr/bin/env python3

#Funcion que calcule el promedio de 2 numeros
#y algunos usos de la funcion

def promedio (n1,n2):
    prom=(n1+n2)/2
    return prom

print (promedio(5,9))

a=promedio(100,58)
b=promedio (a,57)

c=int(input("Ingrese n1: "))
d=int(input("Ingrese n2: "))
e=promedio(c,d)
print(e)

print (promedio(100,20),promedio(200,30))
