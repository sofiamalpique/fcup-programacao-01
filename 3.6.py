from turtle import*

def triangulo(lado):

    for i in range(3):

        forward(lado)
        left(120)
        

def triforce(lado):
    
    triangulo(2*lado)
    penup()
    forward(lado)
    pendown()
    left(60)
    triangulo(lado)
   
    
    
