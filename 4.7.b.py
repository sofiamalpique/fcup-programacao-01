def primo(n):
    d=2
    while n%d!=0:
        d=d+1
    if d==n:
        return True
    else:
        return False
