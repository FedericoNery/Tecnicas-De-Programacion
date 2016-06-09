#!/usr/bin/env python3

#8 Pensar los ej 1, 2, 3 como funciones que reciben todos los datos necesarios
#para el dibujo (coordenadas de inicio, tamaño, color, etc.)

import turtle

t=turtle.Turtle()

def CrearRectangulo (base,altura,x,y,color):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.color(color)
    for r in range(2):
        t.fd(base)
        t.rt(90)
        t.fd(altura)
        t.rt(90)
    t.hideturtle()
    
CrearRectangulo(100,50,25,25,"blue")

def CrearDona (radio,ancho,x,y,color):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.pencolor(color)
    t.width (ancho)
    t.circle(radio)
    t.hideturtle()

CrearDona(100,60,50,50,"red")

def CrearPoligono (radio,lados,ancho,x,y,color):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.pencolor(color)
    t.width (ancho)
    t.circle(radio, None, lados)

CrearPoligono (150,8,10,30,30,"yellow")
