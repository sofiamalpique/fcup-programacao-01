def classifica(p):
    if p>=0 and p<50:
        return 'insuficiente'
    elif p>=50 and p<70:
        return 'suficiente'
    elif p>=70 and p<80:
        return 'bom'
    elif p>=80 and p<90:
        return 'muito bom'
    elif p>=90 and p<=100:
        return 'excelente'
    else:
        return 'inválido'
