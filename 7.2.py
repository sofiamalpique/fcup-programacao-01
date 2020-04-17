def media_geom(xs):
    s=1
    n=len(xs)
    for i in range(n):
        s=s*xs[i]
    m=s**(1/n)
    return m
