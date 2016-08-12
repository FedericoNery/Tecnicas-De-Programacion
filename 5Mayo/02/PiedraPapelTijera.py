#!/usr/bin/env python3

#Hacer un programa que permita jugar al piedra papel o tijeras.
#Debe indicar cual es el ganador al mejor de tres.

import random

def PiedraPapelTijera():
    piedra=1
    papel=2
    tijera=3
    listacpu=[piedra,papel,tijera]
    g1=gcpu=0
    
    while (g1<2 and gcpu<2):
        print("------JUGADA------")
        p1=int(input("Piedra=1, Papel=2, Tijera=3 // Jugador1: "))
        indice=random.randrange(0,3)
        pcpu=listacpu[indice]
        print("Eleccion Jugador 1: ",p1)
        print("Eleccion CPU: ",pcpu)
        if ((p1+1==pcpu) or (p1==tijera and pcpu==piedra)):
            gcpu+=1
            print("------GANO CPU------")
        elif ((p1==pcpu+1) or (pcpu==tijera and p1==piedra)):
            g1+=1
            print("------GANO P1------")
        elif (p1==pcpu):
            print("------EMPATE------")

    if g1==2:
        print("------FINAL------")
        print("Ganador Jugador 1!")
    elif gcpu==2:
        print("------FINAL------")
        print("Ganador CPU")
        
       
PiedraPapelTijera()  
