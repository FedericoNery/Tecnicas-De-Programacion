#!/usr/bin/env python3

# calcula el cuadrado
# de un nro.

try:
    a = float(input("ingrese número: "))    
except:
    print("ingresá un número")
else:
    print("El cuadrado de ",a," es ", a*a)
finally:
    print("siempre pase lo que pase")
    

        
