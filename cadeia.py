def primeira(c, txt):
    for i in range(len(txt)):
        if txt[i] == c:
            return i
    return -1
