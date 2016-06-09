#!/usr/bin/env python3

#6 Dos palabras son anagramas si se pueden reordenar las letras de una palabra
#para formar la otra. Escriba una función llamada es_anagrama que tome dos
#cadenas y retorne True si son anagramas y False en caso contrario.

cadena1 = "eaabcdb"
cadena2 = "dcbaaeb"

def EsAnagrama (cadena1,cadena2):
    if len(cadena1)!=len(cadena2):
        return False
    lista1 = [caracter for caracter in cadena1]
    lista2 = [caracter for caracter in cadena2]
    if sorted(lista1)==sorted(lista2):
        return True
    else:
        return False

EsAnagrama(cadena1,cadena2)
