from math import*

def desvio_padrao(xs):
    n=len(xs)
    s1=0
    s2=0
    for i in range(n):
        s1=s1+xs[i]
    m=s1/n
    for i in range(n):
        s2=s2+(xs[i]-m)**2
        print(s2)
    D=sqrt((1/(n-1))*s2)
    return D
