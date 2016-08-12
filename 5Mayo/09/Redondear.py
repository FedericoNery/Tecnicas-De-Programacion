#!/usr/bin/env python3

#6 Hacer una función que redondee un número decimal F a una cantidad D de
#decimales.
 
#redondear(14.672, 1) -> 14.7
#redondear(14.672, 2) -> 14.67
#redondear(14.679, 0) -> 14

F=float(input("Ingrese numero: "))
D=int(input("Ingrese decimales: "))

def Redondear(F,D):
    F=round(F,D)
    return F

##def Redondear(F,D):
##    auxF=str(F)
##    largo=len(auxF)
##    decimal=int(auxF[-D])
##    decimalant=int(auxF[-D-1])
##    if decimal>=5:
##        decimalant=str(decimalant+1)
##    else:
##        decimalant=str(decimalant)
##    nuevoF=auxF[-D:0]+decimalant
##    print(nuevoF)

Redondear(F,D)
    
