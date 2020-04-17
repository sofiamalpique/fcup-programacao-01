def contar(txt):
    ORD=[65,69,73,79,85,97,101,105,111,117]
    v=0
    c=0
    e=0
    for i in range(len(txt)):
        ord(txt[i])
        if ord(txt[i]) in ORD:
            v=v+1
        if (65<ord(txt[i])<=90 or 97<ord(txt[i])<=122) and ord(txt[i]) not in ORD:
            c=c+1
        if ord(txt[i]) not in ORD and not(65<ord(txt[i])<=90 or 97<ord(txt[i])<=122):
            e=e+1
    print("tem",v,"vogais, tem",c,"consoantes e tem",e,"caracteres especiais")
