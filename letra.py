def letra(c):
    if (c>='a' and c<='z') or (c>='A' and c<='Z'):
        return True
    else:
        return False

def palavras(txt):
    lst=[]
    s=''
    i=0
    while i<len(txt):
        print(i)
        if letra(txt[i]):
            print(txt[i])
            s=s+txt[i]
            print(s)
        else:
            lst.append(s)
            s=''
        if i==(len(txt)-1) and letra(txt[i]):
            lst.append(s)
        i=i+1
    return lst    
