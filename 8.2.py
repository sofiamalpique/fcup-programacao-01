def collatz(n):
    lst=[]
    p=n
    lst.append(p)
    while p!=1:
        if p%2==0:
            p=int(p/2)
            lst.append(p)
        else:
            p=int(p*3+1)
            lst.append(p)
            
    lst.append(1)
    return(lst)
