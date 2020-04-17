from math import*

def radianos(graus,minutos,segundos):

    m =  minutos/60

    s = segundos/3600

    g = graus + m + s

    r = (g*pi)/180

    return r
