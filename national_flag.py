import turtle
t=turtle.Turtle()

t.pencolor("black")
def rectangle(x,y,color,length,weidth,pen_color="black"):
    t.up()
    t.goto(x,y)
    t.down()
    t.pencolor(pen_color)
    t.begin_fill()
    t.color(color)
    t.forward(length)
    t.left(90)
    t.forward(weidth)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(weidth)
    t.left(90)
    t.end_fill()
    
rectangle(-50,0,"orange",400,70)
rectangle(-50,-70,"white",400,70)
rectangle(-50,-140,"green",400,70)
turtle.done()

t.circle