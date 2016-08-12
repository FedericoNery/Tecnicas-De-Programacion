#!/usr/bin/env python3

#2. Leer el archivo creado y mostrarlo en pantalla.

lista=[]
f=open("uno.txt","r")
lista=f.readlines()
for item in lista:
    print(item)
f.close()
