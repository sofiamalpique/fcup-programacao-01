def repetidos(lista):
    a=0
    lst=sorted(lista)
    for i in range(len(lst)-1):
        if lst[i]==lst[i+1]:
            a=a+1
    if a!=0:
        return True
    else:

        return False
