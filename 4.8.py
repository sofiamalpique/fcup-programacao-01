def leibniz(k):
    s=0
    for i in range(k+1):
        s=s+4*(((-1)**i)/(2*i+1))

    return s
