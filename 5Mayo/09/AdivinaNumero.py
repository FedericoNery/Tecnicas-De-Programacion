#!/usr/bin/env python3

#8 Hacer un programa que genere un número de N cifras y pregunte al usuario
#números hasta que lo adivine. Mostrar la cantidad de intentos usados para
#adivinar el número.

import random


      
def AdivinarNro():
    N=int(input("Ingrese la cantidad de cifras: "))
    numero=intentos=0
    usuario=" "
    for i in range (N):
          numero+=random.randrange(0,10)*(10**i)
#    print(numero) //para saber que numero es antes del while
    numero=str(numero)
    while (usuario!=numero):
          usuario=str(input("Ingrese numero: "))
          intentos+=1
    print("La cantidad de intentos fue de %d veces" % intentos)
    print("El numero es: " + usuario)

AdivinarNro()
          
          
    
