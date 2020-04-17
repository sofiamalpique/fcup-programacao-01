def ocorrencia(txt,c):
    X=[]
    for i in range(len(txt)):
        if txt[i]==c:
            X.append(i)
    return X
