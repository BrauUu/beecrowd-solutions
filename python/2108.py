biggest = ''
while True:
    x = input().split()
    
    if x[0] == '0':
        break
    
    res = ''
    for i in range(len(x)):
        item = x[i]
        res += str(len(item)) + ('-' if i < len(x) - 1 else '')
        if len(item) >= len(biggest):
            biggest = item
    print(res)

print()   
print(f'The biggest word: {biggest}')