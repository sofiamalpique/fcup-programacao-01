def ocorrencias(txt,c):
    o=[]
    for i in range(len(txt)):
        if txt[i]==c:
            o.append(i)
    return o
