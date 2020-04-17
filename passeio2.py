from random import*
from turtle import*

def visivel():
    w = 0.5*window_width()
    h = 0.5*window_height()
    x = xcor()
    y = ycor()
    return (x<w and x+w>=0 and y<h and y+h>=0)

def passei(n,a):
    step=10
    for i in range (n):
        forward(step)
        if visivel():
            angle = randint(-a,a)
            left(angle)
        else:
            angle = towards(0,0)
            setheading(angle)
