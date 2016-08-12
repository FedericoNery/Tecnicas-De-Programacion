#!/usr/bin/env python3

#3. Hacer un programa que genere otro programa en python que muestre la tabla
#de multiplicar de un numero ingresado por teclado.

f=open("TablaMulti.py","w")
tabla=int(input("Ingrese numero: "))
lista=[]
for i in range(1,11):
    lista.append(str(tabla)+" * "+str(i)+" = "+str(tabla*i)+"\n")
f.writelines(lista)
f.close()
