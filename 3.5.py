from turtle import*


def triangulo(lado):

    for i in range(3):

        forward(lado)
        left(120)


def quadrado(lado):
    for i in range(4):

        forward(lado)
        left(90)
        

def casa(lado):
    quadrado(lado)
    left(90)
    penup()
    forward(lado)
    pendown()
    right(90)
    triangulo(lado)
    
