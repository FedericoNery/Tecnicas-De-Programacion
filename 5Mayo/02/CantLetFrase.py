#!/usr/bin/env python3

#Hacer una función que cuente la cantidad de apariciones de cada caracter en
#una frase

frase = "ella el la el la la"

def CantLetFrase(frase):
    diccio={}
    letras=[caracter for caracter in frase if not caracter==" "]
    while (letras != []):
        cant=letras.count(letras[0])
        word=letras[0]
        for a in range(0,cant):
            letras.remove(word)
        diccio [word]=cant
    print (diccio)

CantLetFrase(frase)

def CodeCantLetFrase(frase):    
    letras={}
    for le in frase:
        if le in letras.keys():
            letras[le] = letras[le]+1
        else:
            letras[le]=1
    print (letras)

CodeCantLetFrase(frase)
