def triangular(n):
    k=0
    s=0
    while n>s:
        k+=1
        s+=k
    if s==n:
        return True
    else:
        return False
    
        
