#!/usr/bin/env python3

#Crear una lista de 10 elementos aleatorios entre 1 y 10
#Mostrar:
#-La lista ordenada
#El numero mayor
#El numero menor
#Cuantas veces aparece en la lista el numero mayor

import random

def Aleatorio():
    lista=[]
    for i in range (1,21):
        numero = random.randrange(1,11)
        lista.append(numero)
    print (sorted(lista))
    print ("El menor es: ",min(lista))
    print ("El mayor es: ",max(lista))
    print ("El mayor aparece %d veces" % lista.count(max(lista)))

Aleatorio()
    
    
