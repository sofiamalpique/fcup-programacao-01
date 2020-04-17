def filtra_letras(txt):
    s=0
    for i in txt:
        if (i>='a' and i<='z') or (i>='A' and i<='Z'):
            s=s+1
    if s==len(txt):
        return True
    else:
        return False
