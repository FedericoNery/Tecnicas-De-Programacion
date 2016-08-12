#!/usr/bin/env python3

# calcula 20 dividido un numero 
# ingresado desde teclado

try:
    a = float(input("ingrese número: "))   
except ValueError:
    print("ingresá un número")

try:
    print("20 / ", a," = ", 20 / a)
except ZeroDivisionError:
    print("no se puede dividir por cero")    
except NameError:
    pass


