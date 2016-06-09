#!/usr/bin/env python3

#1 Mostrar los numeros pares desde un numero N hasta un numero M.
#M y N se ingresan desde teclado
#Intentar resolverlo de 2 o mas formas

n=(int(input("Ingrese N: ")))
m=(int(input("Ingrese M: ")))

for a in (range(n,m)):
    if (a%2==0):
          print (a)
