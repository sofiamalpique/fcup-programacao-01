def dup_vogais(txt):
    vogais=['a','e','i','o','u','A','E','I','O','U']
    lst=[]
    for i in txt:
        lst.append(i)
        if i in vogais:
            lst.append(i)
    return ''.join(lst)
