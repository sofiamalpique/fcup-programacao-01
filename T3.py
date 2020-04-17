def primo(n):
    d=0
    for i in range(1,n+1):
        if n%i==0:
            d=d+1
    if d==2:
        return True
    else:
        return False
        
def proximo_primo(n):
    s=n+1
    while primo(s)==False:
        s=s+1
    return s
