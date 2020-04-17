def algarismos(n):
    s=0
    while n!=0:
        s=s+1
        n= n//10
    return s
