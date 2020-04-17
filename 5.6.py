def filtra_letras(txt):
    x=''
    for i in txt:
        if (i>='a' and i<='z') or (i>='A' and i<='Z'):
            x=x+i
    return x
