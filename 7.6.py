def magico(A):

    #primeira diagonal:
    s=0
    for i in range(0,len(A)):
        s=s+A[i][i]

    #segunda diagonal:
    s2=0
    for i in range(0,len(A)):
        s2=s2 + A[i][len(A)-i-1]
        #fica [len(A)-i-1] porque assim obtemos os extremos
    if s2!=s:
        return False

    #linhas:
    for i in range(0,len(A)):
        sumlin=0
        for j in range(0,len(A)):
            sumlin=sumlin+A[i][j]
        if (sumlin!=s):
            return False
        #antes da soma reiniciar, ela verifica se é igual à
        #das diagonais!

    #colunas:
    for i in range(0,len(A)):
        sumcol=0
        for j in range(0,len(A)):
            sumcol=sumcol+A[j][i]
            #vai ver o elemento 0 da linha 0, 1 e 2, que são
            #as colunas! Uma coluna é composta pela mesma posição
            #de elementos, mas de linhas diferente, daí interessar
            #fixar a posição do elemento e variar a linha
        if sumcol!=s:
            return False
    return True
