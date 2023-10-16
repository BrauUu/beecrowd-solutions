while True:
    exp = input()
    n1 = int(exp[exp.index('+') - 1::-1])
    n2 = int(exp[exp.index('=') - 1:exp.index('+'):-1])
    res = int(exp[:exp.index('='):-1])
    print(n1 + n2 == res)     
    if n1 == n2 == res:
        break   