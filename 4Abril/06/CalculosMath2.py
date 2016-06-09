#!/usr/bin/env python3

import math

lado1 = int(input('Ingrese un valor: '))
lado2 = input("Ingrese el segundo lado: ")
lado2 = int(lado2)
lado3 = int(input("Ingrese el tercero: "))
perimetro = lado1 + lado2 + lado3

print("El perimetro de un triangulo")
print("de lados %d, %d, %d es: %03d" % (lado1, lado2, lado3, perimetro))

print("-" * 40 )

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

print("La superficie de un triangulo")
print("de base %3.2f y altura %3.2f es: %3.2f" % (base, altura, base * altura / 2), end='')


print("-" * 40 )

radio = int(input("Ingrese el radio: "))
print("El perimetro de un circulo")
print("de radio {1} es: {0}".format(radio, 2 * math.pi * radio), end='')
#print(2 * math.pi * 9)

print("-" * 40 )

print("La superficie de un circulo")
print("de radio 9 es ", end='')
print(math.pi * 9 ** 2)


