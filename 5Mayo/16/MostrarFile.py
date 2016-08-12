#!/usr/bin/env python3

#Hacer un programa que muestre las líneas del archivo:
#https://drive.google.com/file/d/0B7VxfVNCFEcibGxHRmZxdklRQ2c/view?usp=sharing
#Que tengan más de 10 caracteres de longitud y no empiezan en 'p'

file=open("ejemplo_01.py","r")
for line in file:
    i=0
    aux=" "
    if len(line)>10:
        while aux<"a" or aux>"z":
            aux=line[i]
            i+=1
        if aux!="p":
            print(line[i-1:])

file.close()
