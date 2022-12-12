def draw_circle(x, y,color, radius):
    t.up()
    t.goto(x,y)
    t.begin_fill()
    t.fillcolor(color)
    t.down()
    t.circle(radius)
    t.end_fill()

import turtle
t=turtle.Turtle()
window=turtle.Screen()
window.title("Sharma's Graphics")

draw_circle(0,-50,"red",50)
draw_circle(200,200,"green",50)
draw_circle(-200,200,"yellow",50)
draw_circle(-200,-200,"orange",-50)
draw_circle(200,-200,"pink",-50)