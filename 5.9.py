def palindromo(txt):
    tf=''
    for i in txt:
        if (i>='a' and i<='z') or (i>='A' and i<='Z'):
            tf=tf+i
    tf=tf.lower()
    I=''
    for i in range(1,len(tf)+1):
        I=I+tf[-i]
    if I==tf:
        return True
    else:
        return False
