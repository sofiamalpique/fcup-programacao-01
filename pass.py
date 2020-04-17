def forte(txt):
    if len(txt)>=8:
        a=0
        b=0
        c=0
        for i in range(len(txt)):
            if txt[i] >= "A" and txt[i]<="Z":
                a= a+1
            elif txt[i] >= "a" and txt[i]<= "z":
                b= b+1
            elif txt[i] >= "0" and txt[i]<= "9":
                c = c +1
        if a!=0 and b!=0 and c!=0:
            return True
        else:
            return False

    else:
        return False
