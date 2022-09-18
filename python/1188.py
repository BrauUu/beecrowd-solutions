caracter = input()
arrList = []

for x in range(12):
    arrList.append([])
    for y in range(12):
        arrList[x].append(float(input()))
    
sum = 0
count = 0
    
for x in range(7, 12):
    w = x - ((x - 6) * 2) 
    for y in range(w, x):
        sum = sum + arrList[x][y]
        count = count + 1
if(caracter == 'S'):
    print(f'{sum:.1f}');
else:
    if (caracter == 'M'):
        print(f'{(sum / count):.1f}')