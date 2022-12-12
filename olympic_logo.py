def draw_circle(x, y,color, radius):
    t.up()
    t.goto(x,y)
    t.pencolor(color)
    t.pensize(10)
    t.down()
    t.circle(radius)

import turtle
t=turtle.Turtle()
window=turtle.Screen()
window.title("Sharma's Graphics")

draw_circle(0,0,"black",50)
draw_circle(120,0,"red",50)
draw_circle(-120,0,"blue",50)

draw_circle(-60,50,"orange",-50)
draw_circle(60,50,"green",-50)