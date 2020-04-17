def IMC(m,a):
    I=m/a**2
    if I<18.5:
        return "abaixo"
    elif 18.5<=I<25:
        return "normal"
    elif 25<=I<30:
        return "sobrepeso"
    else:
        return "obesidade"
    
