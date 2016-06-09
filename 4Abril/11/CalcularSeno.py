#!/usr/bin/env python3

#Se ingresa un angulo, si es mayor a 1, asumir que es en grados,
#de lo contrario usar radianes. Calcular el seno.

import math

angulo = float(input("Ingrese un angulo: "))

if angulo>1:
    print("El seno de %f  grados es de %f ",math.sin(math.radians (angulo)))
else:
    print("El seno del angulo en radianes es: ", math.sin(angulo))
