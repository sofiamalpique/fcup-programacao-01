def inversa(txt):
    I=''
    for i in range(1,len(txt)+1):
        I=I+txt[-i]
    return I
