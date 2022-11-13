while True:
    n = int(input())

    if n == 0:
        break

    sum = 0

    VALUES = {
        'suco de laranja': 120,
        'morango fresco': 85,
        'mamao': 85 ,
        'goiaba vermelha': 70,
        'manga': 56,
        'laranja':	50 ,
        'brocolis': 34 
    }

    for i in range(n):
        y = input()
        q = y[:(y.find(' '))]
        x = y[(y.find(' ')) + 1:]

        sum += int(q) * VALUES[x]
    
    if sum > 130:
        print(f'Menos {sum - 130} mg')
    elif sum < 110:
        print(f'Mais {110 - sum} mg')
    elif sum >= 110 and sum <= 130:
        print(f'{sum} mg')
