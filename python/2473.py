flavinhoBet = list(map(int, input().split()))
chosenNumbers = list(map(int, input().split()))

count = 0

for number in chosenNumbers:
    if flavinhoBet.count(number) > 0:
        count += 1
        
match count:
    case 3:
        print('terno')
    case 4:
        print('quadra')
    case 5:
        print('quina')
    case 6:
        print('sena')
    case _:
        print('azar')