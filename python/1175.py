arr = []

for i in range(20):
    arr.append(int(input()))
    
arr.reverse()

for i in range(20):
    print(f'N[{i}] = {arr[i]}')