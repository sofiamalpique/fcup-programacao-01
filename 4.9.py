from random import*
def soma2dados(k):
    p=0
    for i in range(100): #o 100 é o número de vezes em que vamos lançar os dados
        d1=randint(1,6)
        d2=randint(1,6)
        if d1+d2==k:
            p=p+1
    print("frequencia =", p/100)
    
#A experiência passa por estudar quantas vezes em 100 acertamos na soma dos
#dados, ou seja, lanço dois dados simultaneamente e "aposto" que a soma será 3
# em 100 lançamentos ver quantas vezes efetivamente a sua soma dá 3.
