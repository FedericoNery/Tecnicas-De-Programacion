#!/usr/bin/env python3

#6 Pedir al usuario que ingrese cantidad de lados y radio
#y dibujar el polígono correspondiente.

#7 Al anterior agregar: que permita ingresar
#coordenadas de inicio y color

import turtle

t=turtle.Turtle()

lados = int(input("Ingrese cantidad de lados: "))
radio = int(input("Ingrese el radio: "))

x = int(input("Ingrese coordenada X: "))
y = int(input("Ingrese coordenada Y: "))
color = input("Ingrese el color: ")

t.penup()
t.setposition(x,y)
t.pendown()
t.color(color)
t.circle(radio, None, lados)
t.hideturtle()

    
    



        

