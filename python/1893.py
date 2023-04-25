x, y = list(map(int, input().split()))

if y < 3:
    print('nova')
elif y > 96:
    print('cheia')
elif y >= 3 and y <= 96:
    if y - x >= 0:
        print('crescente')
    elif y - x < 0:
        print('minguante')