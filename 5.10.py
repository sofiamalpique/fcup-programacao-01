def rem_espacos(txt):
    c0=''
    l=[]
    for c in txt:
        if c0!=' ' or c!=' ':
            l.append(c0)
        c0=c
    return ''.join(l)
