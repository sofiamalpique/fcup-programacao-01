def algarismos(n):
    s=0
    while n!=0:
        n=n//10
        s=s+1
    return s
