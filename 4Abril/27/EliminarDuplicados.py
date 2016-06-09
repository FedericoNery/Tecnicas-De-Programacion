#!/usr/bin/env python3

#7 Escriba una función llamada eliminar_duplicados que reciba una lista y
#retorne una nueva lista con los elementos únicos de la original. No necesitan
#estar en el mismo orden.

lista=[1,2,1,4,3,7,6,5,6,4,3,2]

def EliminarDuplicados(lista):
    listanueva = set(lista)
    return listanueva

EliminarDuplicados(lista)
