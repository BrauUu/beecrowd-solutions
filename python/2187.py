i = 1
while True:
    n = int(input())
    if n == 0:
        break
    count50 = n // 50
    n = n - count50 * 50
    count10 = n // 10
    n = n - count10 * 10
    count5 = n // 5
    n = n - count5 * 5
    count1  = n // 1
    n = n - count1 * 1
    
    print(f'Teste {i}')
    i += 1
    print(f'{count50} {count10} {count5} {count1}')
    print()
    
    