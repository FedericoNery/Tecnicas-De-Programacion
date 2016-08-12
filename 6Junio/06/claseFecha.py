#!/usr/bin/env python3

#Crear una clase Fecha con:
#atributos:dia, mes, año
#Metodos:mostrar, sumar dias, restar dias
#Hacer un  programa que use objetos de esta clase para demostrar su funcionalidad

class Fecha:
    def __init__(self,dia,mes,anio):
        self.dia=dia
        self.mes=mes
        self.anio=anio
    def mostrar(self):
        print("Hoy: "+str(self.dia)+"-"+str(self.mes)+"-"+str(self.anio))
    def sumarDias(self):
        
    def restarDias():
        pass

a=Fecha(26,5,1993)
b=Fecha(3,5,1994)
print("Dia:",a.dia)
print("Mes:",a.mes)
print("Año:",a.anio)
a.mostrar()
print("-"*10)
print("Dia:",b.dia)
print("Mes:",b.mes)
print("Año:",b.anio)
b.mostrar()
