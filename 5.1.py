def triangular(n):
    k=0
    s=0
    while s<n:
        k=k+1
        s=s+k
    if s==n:
        return True
    else:
        return False
