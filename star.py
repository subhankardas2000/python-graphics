import turtle

star=turtle.Turtle()

star.pensize(10)
star.begin_fill()
star.color("red")
for i in range(5):
    star.forward(100)
    star.right(144)
star.end_fill()
star.penup()
turtle.done()