def elimrep(xs):
    ys=[]
    for x in xs:
        if not(x in ys):
            ys.append(x)
    return ys
