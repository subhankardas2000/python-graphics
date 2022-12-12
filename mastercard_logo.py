import turtle
t=turtle.Turtle()

def mastercard(x,y,color,rad):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.pencolor(color)
    t.circle(rad)
    t.end_fill()
    
    
mastercard(0,0,"red",100)
mastercard(120,0,"orange",100)
turtle.done()