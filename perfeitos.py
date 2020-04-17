def divisores(n):
    k=[]
    for i in range(1,n+1):
        if n%i==0:
            k.append(i)
    return k

def perfeito(n):
    if sum(divisores(n))== 2*n:
        return True
    else:
        return False
