n = int(input())

arr = [1, 1]

for i in range(2,n):
    arr.append(arr[i-1] + arr[i-2])
    
res = ''
    
for i in range(n, 0, -1):
    if i == 1:
        res += str(arr[i - 1])
        continue
    res += f'{str(arr[i - 1])} '
    
print(res)
