color_list=["yellow", "green", "red", "blue"]

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

draw_circle(0,0,color_list[0],50)
draw_circle(100,0,color_list[1],50)
draw_circle(-100,0,color_list[2],50)
draw_circle(-200,0,color_list[3],50)