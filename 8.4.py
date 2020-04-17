i=[]

def collatz(n):
    if n==1:
        return i
    if n%2 == 0:
        n = n //2
        i.append(n)
    else:
        n= n*3 +1
        i.append(n)
    return collatz(n)


print(collatz(n))
