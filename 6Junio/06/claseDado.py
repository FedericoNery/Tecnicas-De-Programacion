#!/usr/bin/env python3

##import random
##
##def tirar():
##    return random.randrange(1,7)
##print (tirar())
##como se hace esto con clases??

import random

class Dado:
    #Constructor (__init__)
    #Se ejecuta al crear un objeto de esta clase
    def __init__(self,lados):
        self.cant_caras=lados
        self.numero=random.randrange(1,self.cant_caras+1)
    def tirar(self):
        self.numero=random.randrange(1,self.cant_caras+1)
        
##    atributos:
##        numero
##        cantidad de caras
##    metodos:
##        tirar

#Instanciar un objeto clase Dado
#a es un objeto clase Dado
a=Dado(6)
b=Dado(6)
print(a.numero)
print(b.numero)
b.tirar()
print(b.numero)
