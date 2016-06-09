#!/usr/bin/env python3

#2 Informar la cantidad de letras de una frase que ingresa por teclado.
#Mostrar las primeras cinco letras de la misma.
#Uso la funcion del ejercicio LimpiarMas.py

frase=(str(input("Ingrese frase: ")))

def limpiarMas (frase):
    copia=""
    for a in frase:
        if ((a!=' ') and (a!=',') and (a!='.') and (a!=';')):
            copia+=a
    return (copia)

s=limpiarMas (frase)
print("La cantidad de letras es: ",len(s))
print ("Las primeras 5 letras son:",s[:5])


