#!/usr/bin/env python3

# calcula el cuadrado
# de un nro.

while True:
    try:
        a = float(input("ingrese número: "))
        print("El cuadrado de ",a," es ", a*a)        
    except ValueError:
        print("Error. Ingresá un número")
    except KeyboardInterrupt:
        print("chau maestro!!")
        quit()
    except Exception as error:
        print(type(error), error)



        
