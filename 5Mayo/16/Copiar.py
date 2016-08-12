#!/usr/bin/env python3

#b. Hacer un programa que copie las primeras dos líneas del archivo de (a) a
#otro archivo "dos.txt"

a=open("uno.txt","r")
b=open("dos.txt","w")
frase=" "
for i in range(2):
    frase=a.readline()
    b.write(frase)
    frase=" "
a.close()
b.close()
