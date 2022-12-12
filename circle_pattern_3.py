import turtle
t=turtle.Turtle()

color_list=["yellow", "green", "red", "blue","black"]

t.up()
t.goto(200,0)

for i in range(5):
    t.down()
    t.color(color_list[i])
    t.pensize(20)
    t.circle(100)
    
    t.up()
    t.backward(100)
    