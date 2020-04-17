def bissect(f,a,b,eps):
    #Método de bisseções para f(x)=0 em [a,b]
    while b-a>eps:
        m = (a+b)/2
        if f(a)*f(b) < 0:
            b = m
        else:
            a = m
    return m
