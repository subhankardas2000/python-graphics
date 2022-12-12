from turtle import *
from math import atan2,degrees

D = 0.1 #bezier step
R = '#ED1B38'
B = '#005993'
W = '#FFFFFF'
K = '#000000'
def Bez(a,b,c,d):
    up()
    goto(a)
    down()
    t = 0.0
    while t <= 1.0:
        t3 = t**3
        t2 = t**2
        f1 = -t3+3*t2-3*t+1
        f2 = 3*t3-6*t2+3*t
        f3 = -3*t3+3*t2
        f4 = t3
        x = a[0]*f1+ b[0]*f2 + c[0]*f3 + d[0]*f4
        y = a[1]*f1 + b[1]*f2 + c[1]*f3 + d[1]*f4
        d1 = -3*t2+6*t-3
        d2 = 9*t2-12*t+3
        d3 = -9*t2+6*t
        d4 = 3*t2
        dx = a[0]*d1+ b[0]*d2 + c[0]*d3 + d[0]*d4
        dy = a[1]*d1 + b[1]*d2 + c[1]*d3 + d[1]*d4
        angr = atan2(dy,dx)
        seth(degrees(angr))
        goto(x, y)
        t+=D
    goto(d)

def Pepsi(sz):
    color(W)
    up()
    seth(0)
    fd(sz)
    lt(90)
    down()
    begin_fill()
    circle(sz)
    end_fill()
    up()
    color(R)
    lt(90)
    fd(sz)
    rt(126.7)
    fd(sz*0.95)
    lt(90)
    down()
    begin_fill()
    circle(sz*0.95,163.1)
    p = pos()
    pts = [p,p+(sz*0.74275,sz*0.2308),p+(sz*1.14545,sz*0.74895),p+(sz*1.33245,sz*1.32555)]
    Bez(*pts)
    end_fill()
    up()
    color(B)
    seth(233.3)
    fd(sz*0.95)
    rt(13.3)
    fd(sz*0.95)
    lt(90)
    down()
    begin_fill()
    circle(sz*0.95,173)
    p = pos()
    pts = [p,p+(sz*0.10705,sz*-0.35325),p+(sz*-0.0774,sz*-0.6761),p+(sz*-0.38725,sz*-0.8211)]
    Bez(*pts)
    p = pos()
    pts = [p,p+(sz*-0.23155,sz*-0.10975),p+(sz*-0.70985,sz*-0.1699),p+(sz*-1.138,sz*-0.30585)]
    Bez(*pts)
    end_fill()
    up()


setup(640,650)
bgcolor(K)
Pepsi(300)
hideturtle()
done()