count = 0
while True:
    try:
        n = int(input())
        sum = 0
        numbers = ''
        for i in range(n, -1, -1):
            if i == 0:
                sum += 1
            sum += i
            numbers = (str(i) + ' ') * i  +  numbers
        count += 1
        num = 'numero' if sum == 1 else 'numeros'
        print(f'Caso {count}: {sum} {num}')
        print('0 ' + (numbers).strip() + '\n')
        
    except:
        break