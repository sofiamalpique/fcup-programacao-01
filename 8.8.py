from typing import*
def filtra(txt):
    tf=''
    for i in txt:
        if (i>='a' and i<='z') or (i>='A' and i<='Z'):
            tf=tf+i
    return tf

def anagramas(txt1,txt2):
    s=0
    t1=txt1.lower()
    t2=txt2.lower()
    str1=filtra(t1)
    str2=filtra(t2)
    if len(str1)!=len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] in str2:
            s=s+1
        if s==len(str2):
            return True
   
        
