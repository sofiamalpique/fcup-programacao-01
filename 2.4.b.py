def soma(n):
    s=0
    for i in range(1,n+1):
        while i<=n:
            s=s+(1/i)
    return s
