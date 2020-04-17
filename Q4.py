def maiordif(lst):
    L=[]
    for i in range(len(lst)-1):
        L.append(abs(lst[i+1]-lst[i]))
    valor=max(L)
    return valor
        
