def aprox(q,n):
    x=q/2
    for i in range(n):
        x=0.5*(x+q/x)
    return x
