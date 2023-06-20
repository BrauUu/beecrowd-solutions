while True:
    x = int(input())

    if x == 0:
        break
    
    arr = []
    
    for i in range(1, x + 1):
        line = ''
        countG = 0
        countWhiteSpaces = int(x/2) - 1
        for g in range(1, x + 1):
            item = ''
            if g - 1 >= x / 2:
                pos = (int(x/2) * 3 + countWhiteSpaces) - (countG) - 1
                item = line[pos - 1: pos + 1] if g >= 10 else line[pos]
                item = (3 - len(item)) * ' ' + item + ' '
                countG += 3
                countWhiteSpaces -= 1
            elif i - 1 >= x / 2:
                ind = x - i
                pos = (g * 3 + g - 1) - 1
                item = arr[ind][pos - 1: pos + 1] if g >= 10 else arr[ind][pos]
                item = (3 - len(item)) * ' ' + item + ' '
            else:
                item = str(g) if g < i else str(i)
                item = (3 - len(item)) * ' ' + item + ' '
            line += item
        line = '  ' + line.strip()
        arr.append(line)
        print(line)
    print()