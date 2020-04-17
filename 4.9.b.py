from random import*
def soma2dados(k):
    p=0
    for i in range(100):
        d1=randint(1,6)
        d2=randint(1,6)
        if d1+d2==k:
            p=p+1
    return(p/100)
freq=[]
for i in range(11):
    v=soma2dados(i+2)
    freq.append(v)
s1=len('soma dos dados')
s2=len('frequencia')+10
print('-'*34)
print('%-*s%*s'%(s1, 'Soma dos dados', s2, 'Frequêcia'))
print('-'*34)
for i in range(11):
    print('%-*d%*.2f' % (s1,i+2,s2,freq[i]))
