def forte(passwd):
    a=0
    b=0
    c=0
    for i in passwd:
        if i>='a' and i <='z':
            a=a+1
        elif i>='A' and i<='Z':
            b=b+1
        elif i>='0' and i<='9':
            c=c+1
    if (a>=1 and b>=1 and c>=1 and len(passwd)>=8):
        return True
    else:
        return False
