def triangulo(a,b,c):
    if a==b and b==c:
        print("equilátero")

    elif a!=b and b!=c and c!=a:
        print("escaleno")

    else:
        print("isósceles")
