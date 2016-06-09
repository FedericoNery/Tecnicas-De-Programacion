#!/usr/bin/env python3

#8 Escriba dos versiones de una función que lea el archivo palabras.txt y
#construya una lista con un elemento por palabra. Una versión usará el método
#append y la otra la construcción t=t+[x]. ¿Cual es mas lenta? ¿Por qué?
#Pista: use el módulo time para medir lo que tarda la ejecución de las versiones

f = open("/home/alumno/Python/4Abril/27/PalabrasArchivo.txt","w")
f.write("uno dos tres cuatro cinco seis")
f.close()

def PalabrasArchivo(f):
    lista=[]
    f = open("/home/alumno/Python/4Abril/27/PalabrasArchivo.txt","r")
    lista = f.read()
    palabras = lista.split()
    f.close()
    print(palabras)

PalabrasArchivo(f)

#Falta hacerlo con append y con t=t+[x]
#Falta usar el modulo time
