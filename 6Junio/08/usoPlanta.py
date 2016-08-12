#!/usr/bin/env python3

#2. hacer un programa que use la clase Planta con tres objetos diferentes de
#esa clase.

from clasePlanta import Planta

flor=Planta(10,1)
rosa=Planta(20,2)
girasol=Planta(30,3)

print("alto= ",flor.alto)
print("hojas= ",flor.hojas)
print("-" *10)
print("alto= ",rosa.alto)
print("hojas= ",rosa.hojas)
print("-" *10)
print("alto= ",girasol.alto)
print("hojas= ",girasol.hojas)
print("-" *10)
flor.crecer()
rosa.crecer()
girasol.crecer()
print("alto= ",flor.alto)
print("alto= ",rosa.alto)
print("alto= ",girasol.alto)
print("-" *10)
flor.crecer(4)
rosa.crecer(4)
girasol.crecer(4)
print("alto= ",flor.alto)
print("alto= ",rosa.alto)
print("alto= ",girasol.alto)
print("-" *10)
flor.crear_hoja()
rosa.crear_hoja()
girasol.crear_hoja()
print("hojas= ",flor.hojas)
print("hojas= ",rosa.hojas)
print("hojas= ",girasol.hojas)
