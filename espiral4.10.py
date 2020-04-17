from turtle import*
def espiral(a):
    size=1
    for i in range (300):
        forward(size)
        right(a)
        size+=1
