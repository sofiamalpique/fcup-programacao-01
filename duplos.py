def dup_vogais(txt):
    a=""
    for i in range(len(txt)):
        if txt[i] == "a":
            a = a + txt[i]
        elif txt[i] == "e":
            a+= txt[i]
        elif txt[i] == "i":
            a+= txt[i]
        elif txt[i] == "o":
            a+= txt[i]
        elif txt[i] == "u":
            a+= txt[i]
        elif txt[i] == "A":
            a+= txt[i]
        elif txt[i] == "E":
            a+= txt[i]
        elif txt[i] == "I":
            a+= txt[i]
        elif txt[i] == "O":
            a+= txt[i]
        elif txt[i] == "U":
            a+= txt[i]
        a += txt[i]
    return a
