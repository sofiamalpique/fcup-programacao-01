def binom(n,k):
    a=1
    b=1
    c=1
    for i in range(1,n+1):
        a=a*i
    for i in range(1,k+1):
        b=b*i
    for i in range(1,n-k+1):
        c=c*i
    C=a/(b*c)
    return int(C)
