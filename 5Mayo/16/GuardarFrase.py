#!/usr/bin/env python3

#1. Hacer un programa que guarde frases en un archivo "uno.txt"

f=open("uno.txt","a")
frase=input("Ingrese su frase: ")
f.write(frase)
f.close()
