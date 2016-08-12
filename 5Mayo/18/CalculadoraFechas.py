#!/usr/bin/env python3

#Intentá hacer una calculadora para fechas. Podrías empezar con una que sume y
#reste fechas (año-mes-día) Se puede ir agregando otras funciones: (ej. sumar
#o restar teniendo en cuenta horario, etc.)

import datetime

def CalculadoraFechas():
    dia1=int(input("dia1: "))
    mes1=int(input("mes1: "))
    anio1=int(input("anio1: "))
    dia2=int(input("dia2: "))
    mes2=int(input("mes2: "))
    anio2=int(input("anio2: "))
    operacion=str(input("s=suma r=resta: "))
    fecha1=datetime.datetime(anio1,mes1,dia1)
    fecha2=datetime.datetime(anio2,mes2,dia2)
    if operacion=="s":
        suma=(fecha1+fecha2)
        print("La suma entre las fechas en años es: ",suma.days/30/365)
        print("La suma entre las fechas en meses es: ",suma.days/30)
        print("La suma entre las fechas en dias es: ",suma.days)
    elif operacion=="r":
        resta=(fecha1-fecha2)
        print("La diferencia entre las fechas en años es: ",resta.days/30/365)
        print("La diferencia entre las fechas en meses es: ",resta.days/30)
        print("La diferencia entre las fechas en dias es: ",resta.days)
    else:
        pass

CalculadoraFechas()
