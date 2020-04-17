from turtle import*

def quadrado(n):
    for i in range (4):
        forward(n)
        right(90)
        
def triangulo(n):
    for i in [1,2,3]:
        forward(n)
        left(120)
def casa(n):
    quadrado(n)
    triangulo(n)
        
