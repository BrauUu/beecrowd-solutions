count = 1
while True:
    a = int(input())
    if a == 0:
        break
    x = input()
    if count > 1:
        print('')
    print(f'Instancia {count}')
    print('verdadeira' if x.count(str(a)) > 0 else 'falsa')
    count += 1
    