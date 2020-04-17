def elimrep(xs):
    i=0
    while i< len(xs):
        if xs[i] in xs[0:i]:
            del xs[i]
        else:
            i+=1
            
