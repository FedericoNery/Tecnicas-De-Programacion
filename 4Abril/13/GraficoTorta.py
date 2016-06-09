#!/usr/bin/env python3

#10 Ingresar 3 valores entre 0 y 100 y generar un gráfico de torta (usar 8.3)

import turtle

t=turtle.Turtle()
u=turtle.Turtle()

def CrearPoligono (radio,porcentaje,ancho,color="black"):
##    t.speed(1)
    arco=0
    arco=(porcentaje*360/100)
    x=t.xcor()
    y=t.ycor()
    t.lt(90)
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.pencolor("black")
    t.fillcolor(color)    
    t.width (ancho)
    t.begin_fill()
    t.fd(radio)
    t.rt(180-arco)
    t.fd(radio)
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.lt(90-arco)
    t.circle(radio,arco)
    t.end_fill()        
    t.hideturtle()


color=["blue","red","green"]
xw=-50
yw=-40
for b in range (3):
    porcentaje=(int(input("Ingrese porcentaje a graficar: ")))
    CrearPoligono (100,porcentaje,3,color[b])
    u.penup()
    u.setposition(xw+(50*b),yw)
    u.pendown()
    u.pencolor(color[b])
    u.write(str(porcentaje)+"%")
    u.hideturtle()


##CrearPoligono (100,60,5,"blue")
##CrearPoligono (100,80,5,"green")
##CrearPoligono (100,120,5,"red")
##CrearPoligono (100,100,5,"orange")
    
