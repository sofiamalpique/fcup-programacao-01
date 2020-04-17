from turtle import*
from random import*

def passeio(n,a):
    #n é o numero de passos e a é o angulo máximo
    step = 10
    for i in range(n):
        forward(step)
        angle = randint(-a,a)
        left(angle)
