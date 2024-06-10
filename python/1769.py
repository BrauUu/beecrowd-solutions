while True:
    try:
        cpf = input()
        digits = []
        for digit in cpf[:-3]:
            if digit.isdecimal():
                digits.append(int(digit))
        b1 = 0 
        b2 = 0
        for i, digit in enumerate(digits):
            b1 += digit * (i + 1)
            b2 += digit * (9 - i)
        b1 = b1 % 11 % 10
        b2 = b2 % 11 % 10
        if b1 == int(cpf[-2]) and b2 == int(cpf[-1]):
            print('CPF valido')
            continue
        print('CPF invalido')

    except:
        break