a, c, x, y = list(map(int, input().split()))

if a + 1 > c - (x + y):
    if x > y / 2:
        print('Caio, a culpa eh sua!')
    else:
        print('Igor bolado!')
else:
    print('Igor feliz!')