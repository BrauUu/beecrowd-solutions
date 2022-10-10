char = input()

arr = []
sum = 0

for i in range(12):
    arr.append([])
    for g in range(12):
        value = float(input())
        arr[i].append(value)
        
        if g < (11 - i):
            sum += value
            
if char == 'M':
    print(f'{(sum / 66):.1f}')
else:
    print(f'{sum:.1f}')
        