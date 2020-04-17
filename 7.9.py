def tempo(t):
    h=t//3600
    print(h)
    m=(t-(h*3600))//60
    print(m)
    s=(t-(h*3600)-(m*60))
    print(s)
    print("%02d:%02d:%02d" % (h,m,s))
