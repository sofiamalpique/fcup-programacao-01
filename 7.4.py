def prod_interno(xs,ys):
    n=len(xs)
    s=0
    for i in range(n):
        s=s+(xs[i]*ys[i])
    return s
