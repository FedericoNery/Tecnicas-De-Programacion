#!/usr/bin/env python3

#10. Hacer un programa que permita jugar al Mastermind:
#Explicación del juego:
#Cada vez que se empieza un partido, el programa debe “eligir” un número de
#cuatro cifras (sin cifras repetidas), que será el código que el jugador debe
#adivinar en la menor cantidad de intentos posibles. 

#Cada intento consiste en una propuesta de un código posible que tipea el
#jugador, y una respuesta del programa. Las respuestas le darán pistas al
#jugador para que pueda deducir el código.

#Estas pistas indican cuán cerca estuvo el número propuesto de la solución a
#través de dos valores: 
#La cantidad de aciertos es la cantidad de dígitos que propuso el jugador que
#también están en el código en la misma posición. 
#La cantidad de coincidencias es la cantidad de digitos que propuso el jugador
#que también están en el código pero en una posición distinta.

#Por ejemplo, si el código que eligió el programa es el 2607, y el jugador
#propone el 1406, el programa le debe responder un acierto (el 0, que está en
#el código original en el mismo lugar, el tercero), y una coincidencia (el 6,
#que también está en el código original, pero en la segunda posición, no en el
#cuarto como fue propuesto). 

#Si el jugador hubiera propuesto  3591, habría obtenido como respuesta ningún
#acierto y ninguna coincidencia,
#ya que no hay números en común con el código original, y si se obtienen
#cuatro aciertos es porque el jugador adivinó el código y ganó el juego.

import random

def Mastermind():
    lista=[0,1,2,3,4,5,6,7,8,9]
    mind=[]
    codigo=[]
    mind.append(lista[random.randrange(0,10)])
    lista.pop(lista.index(mind[0]))
    mind.append(lista[random.randrange(0,9)])
    lista.pop(lista.index(mind[1]))
    mind.append(lista[random.randrange(0,8)])
    lista.pop(lista.index(mind[2]))
    mind.append(lista[random.randrange(0,7)])
    lista.pop(lista.index(mind[3]))
    suma=mind[0]*1000+mind[1]*100+mind[2]*10+mind[3]
    aciertos=coincidencias=0
    while (aciertos<4):
        print("----------")
        aciertos=coincidencias=0
        strcodigo=input("Ingrese codigo: ")
        codigo.clear()
        codigo.append(int(strcodigo[0]))
        codigo.append(int(strcodigo[1]))
        codigo.append(int(strcodigo[2]))
        codigo.append(int(strcodigo[3]))
        print("Codigo propuesto: ",codigo)
        for i in range(4):
            if mind[i]==codigo[i]:
                aciertos+=1
            if mind[i] in codigo and mind[i]!=codigo[i]:
                coincidencias+=1
        print("Coincidencias: ",coincidencias)
        print("Aciertos: ",aciertos)
    print("----------")
    print("Felicitaciones! Acerto el codigo!")
    print("El mind es: ",suma)
        
Mastermind()
