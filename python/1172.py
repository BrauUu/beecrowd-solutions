x = []

for i in range(10):
    y = int(input())
    if y <= 0:
        x.append(1)
    else:
        x.append(y)
        
for i in range(10):
    print(f'X[{i}] = {x[i]}')