#!/usr/bin/env python3

#4 Dibuje un cubo

import turtle

t=turtle.Turtle()

for r in range(4):
    t.fd(100)
    t.rt(90)

t.lt(60)
t.fd(50)
t.rt(60)
t.fd(100)
t.lt(60)
t.bk(50)
t.penup()
t.setposition(100,-100)
t.pendown()
t.fd(50)
t.lt(30)
t.fd(100)

