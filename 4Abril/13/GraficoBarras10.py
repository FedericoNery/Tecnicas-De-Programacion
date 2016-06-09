#!/usr/bin/env python3

#11 Generar un gráfico de barras o torta con hasta 10 valores diferentes
#entre 0% y 100% c/u. Validar entrada de datos.

import turtle

t=turtle.Turtle()
u=turtle.Turtle()

def CrearRectangulo (base,altura,x,y,color="black"):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.color(color,color)
    t.begin_fill()
    for r in range(2):
        t.fd(base)
        t.lt(90)
        t.fd(altura)
        t.lt(90)
    t.end_fill()
    t.hideturtle()

def DibujarFlecha():
    t.begin_fill()
    t.lt(90)
    t.fd(3)
    t.rt(120)
    t.fd(5)
    t.rt(120)
    t.fd(5)
    t.rt(120)
    t.fd(3)
    t.end_fill()

    
t.fd(300)
DibujarFlecha()
t.penup()
t.setposition(0,0)
t.pendown()
t.fd(110)
DibujarFlecha()
t.rt(180)

for a in range(11):
    t.penup()
    t.setposition (-10,10*a)
    t.pendown()
    t.write(10*a, align="right")
    t.fd(300)

t.penup()
t.setposition(0,0)
t.pendown()

color=["blue","red","green","yellow","brown","black","violet","pink","orange","grey"]
distancia=25

for b in range(10):
    porcentaje=(int(input("Ingrese porcentaje a graficar: ")))
    CrearRectangulo (5,porcentaje,distancia,0,color[b])

    u.color(color[b])
    u.penup()
    u.setposition (-100,100-(10*b))
    u.pendown()
    u.write(str(porcentaje)+"%", align="left")

    distancia+=25
    if (b<9):
        pregunta=(input("Desea ingresar otro porcentaje? (S=si, N=no): "))
        if (pregunta=="S"):
            pass
        elif (pregunta=="N"):
            t.penup()
            t.setposition (0,-20)
            t.pendown()
            t.color("black")
            t.write("GRAFICO TERMINADO")
            break
        else:
            print("Respuesta Incorrecta. Fin Grafico")
            break
if (b==9):
    print("Ingreso la cantidad maxima de valores")
t.penup()
t.setposition (0,-20)
t.pendown()
t.color("black")
t.write("GRAFICO TERMINADO")
u.hideturtle()            
