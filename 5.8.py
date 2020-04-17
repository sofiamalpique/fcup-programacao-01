def palindromo(txt):
    I=''
    for i in range(1,len(txt)+1):
        I=I+txt[-i]
    if I==txt:
        return True
    else:
        return False
