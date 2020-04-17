def bissect(f,a,b,eps):
    fa=f(a)
    while b-a>eps:
        m = (a+b)/2
        fm= f(m)
        if fa*fm< 0:
            b=m
        else:
            a=m
            fa=fm
    return m
