#!/usr/bin/env python3

#Hacer una función que reciba una frase y devuelva un diccionario formado por
#pares palabra:cantidad_de_veces

frase = "ella el la el la la"

def CantPalFrase(frase):
    diccio={}
    palabras=frase.split()
    while (palabras != []):
        cant=palabras.count(palabras[0])
        word=palabras[0]
        for a in range(0,cant):
            palabras.remove(word)
        diccio [word]=cant
    print (diccio)

CantPalFrase(frase)

def CodeCantLetFrase(frase):
    palabras={}
    words=frase.split()
    for item in words:
        if item in palabras.keys():
            palabras[item] = palabras[item]+1
        else:
            palabras[item]=1
    print (palabras)

CodeCantLetFrase(frase)
