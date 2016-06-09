#!/usr/bin/env python3

#9 Ingresar 3 valores entre 0 y 100 y generar un gráfico de barras (usar 8.1)

import turtle

t=turtle.Turtle()

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

t.fd(200)
t.penup()
t.setposition(0,0)
t.pendown()
t.lt(90)
t.fd(200)

for a in range(21):
    t.penup()
    t.setposition (-10,10*a)
    t.pendown()
    t.write(10*a, align="right")

t.rt(90)
t.penup()
t.setposition(0,0)
t.pendown()

color=["blue","red","green"]
distancia=25

for b in range (3):
    porcentaje=(int(input("Ingrese porcentaje a graficar: ")))
    CrearRectangulo (5,porcentaje,distancia,0,color[b])
    distancia+=25
    
##CrearRectangulo (5,50,10,0,"blue")
##CrearRectangulo (5,75,60,0,"green")
##CrearRectangulo (5,100,110,0,"red")
