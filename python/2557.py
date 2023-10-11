while True:
    try:
        exp = input()
        if exp == '':
            break
        n1 = exp[:exp.find('+')]
        n2 = exp[exp.find('+') + 1 : exp.find('=')]
        n3 = exp[exp.find('=') + 1 :]
        x = 0
        if n1.isdecimal() and n2.isdecimal():
            x = int(n1) + int(n2)
        elif n1.isdecimal() and n3.isdecimal():
            x = int(n3) - int(n1) 
        elif n2.isdecimal() and n3.isdecimal():
            x = int(n3) - int(n2) 
        print(x) 
    except:
        break