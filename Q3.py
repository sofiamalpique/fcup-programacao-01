def soma(n):
    lst=[]
    for i in range(n):
        if i%2==1:
            lst.append(i**2)
            print(lst)
    S=sum(lst)
    return S
