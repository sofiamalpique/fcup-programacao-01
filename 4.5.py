def bissexto(n):
    if n%4!=0 or (n%4==0 and n%100==0 and n%400!=0):
        return False
    else:
        return True
for n in range(2001,2021):
    if bissexto(n) True:
        print(n)
