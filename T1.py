def quadrantes(x,y):
    if x==0 or y==0:
        return 'EIXOS'
    elif x>=0 and y>=0:
        return 'I'
    elif x<=0 and y>=0:
        return 'II'
    elif x<=0 and y<=0:
        return 'III'
    else:
        return 'IV'
