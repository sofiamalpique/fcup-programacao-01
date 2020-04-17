from math import*

def raiz(q,E):
    x0=q/2
    x1=(1/2)*(x0+q/x0)
    while abs(x1-x0)>=E:
        x0=x1
        x1=(1/2)*(x0+q/x0)
    return x1
