line = int(input())
char = input()

arr = []

for i in range(12):
    arr.append([])
    for g in range(12):
        arr[i].append(float(input()))
        
sum = 0
        
for i in range(12):
    sum += arr[line][i]

if char == 'S':
    print(f'{sum:.1f}')
elif char == 'M':
    print(f'{(sum / 12):.1f}')