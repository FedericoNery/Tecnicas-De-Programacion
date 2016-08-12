#!/usr/bin/env python3

#Linux tiene un programa (línea de comandos) llamado cal que, entre otras cosas,
#muestra un calendario. Correlo y tratá de imitarlo en python.
#Mirá el man de cal y tratá de incorporar alguna de estas funcionalidades
#a tu programa en python.

import datetime

def Calendario():
    fecha=datetime.datetime.now()
    nroMes=fecha.month-1
    listaMes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
              "Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    anio=str(fecha.year)
    dias=" "
    print("    "+listaMes[nroMes]+" "+anio+"    ")
    print(" do lu ma mi ju vi sa")
    for i in range(1,32):
        if i<10:
            dias=dias+str(i)+"  "
        else:
            dias=dias+str(i)+" "
        if i%7==0:
            print(dias)
            dias=" "

Calendario()
