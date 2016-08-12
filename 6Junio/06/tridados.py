#!/usr/bin/env python3

#3 dados contra la CPU, el numero mas alto gana

import random

dadoP1=dadoCPU=i=ganoP1=ganoCPU=0
nrosP1=[]
nrosCPU=[]
while ganoP1<2 and ganoCPU<2:
        dadoP1=random.randrange(1,6+1)
        dadoCPU=random.randrange(1,6+1)
        nrosP1.append(dadoP1)
        nrosCPU.append(dadoCPU)
        i+=1
        if dadoP1>dadoCPU:
            ganoP1+=1
        elif dadoP1<dadoCPU:
            ganoCPU+=1
        else:
            pass
print("P1: ",nrosP1)
print("CPU: ",nrosCPU)
if ganoP1==2:
    print("---GANO P1---")
if ganoCPU==2:
    print("---GANO CPU---")


    
