def mdc(a,b):
    A=[]
    B=[]
    C=[]
    for i in range(1,a+1):
        if a%i==0:
            A.append(i)
    for i in range(1,b+1):
        if b%i==0:
            B.append(i)
    for i in range(len(A)):
        if A[i] in B:
            C.append(A[i])
    return max(C)


def coprimos(n):
    lst=[]
    for i in range(1,n):
        if mdc(i,n)==1:
            lst.append(i)
    return lst
