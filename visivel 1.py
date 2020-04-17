from turtle import*
def visivel():
    w = 0.5*window_width()
    h = 0.5*window_height()
    x = xcor()
    y = ycor()
    return (x<w and x+w>=0 and y<h and y+h>=0)
