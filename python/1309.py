while True:
    try:
        dol = input()
        cents = input()

        res = ''

        for i in range(len(dol), -1, -3):
            if i-3 <= 0:
                res = dol[:i] + res
            else:
                res = ',' + dol[i-3:i] + res

        print(f'${res}.{"0" + cents if len(cents) == 1 else cents}')
    except:
        break