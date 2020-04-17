name = input('what is your name?')
def vogal(name):
    vogais = ["A","E","I","O","U","a","e","i","o","u"]
    s=0
    X=[]
    for i in range(len(name)):
        if name[i] in vogais:
            X.append(i)
            s+=1
    return print("O número de vogais de", name,"são", s,", as vogais são",X)
            
vogal(name)
