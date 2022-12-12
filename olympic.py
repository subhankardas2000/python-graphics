import turtle
a=turtle.Turtle()
b=turtle.Screen()
a.pencolor("white")
#b.bgcolor("black")


def circle(x,rad,color):
    a.up()
    a.pensize(5)
    a.color(color)
    a.forward(x)
    a.down()
    a.circle(rad)

circle(0,50,"black")
circle(120,50,"red")
circle(-240,50,"blue")

a.right(60)
circle(30,50,"yellow")

a.left(50)
circle(155,50,"green")

#turtle.done()