#!/usr/bin/env python3

#5 Dibujar un cilindro

import turtle

t=turtle.Turtle()

t.circle(50)
t.penup()
t.setposition(150,29)
t.pendown()
t.circle(50,180)
t.lt(10)
t.fd(155)

t.penup()
t.setposition(0,0)
t.pendown()

t.rt(180)
t.fd(155)
