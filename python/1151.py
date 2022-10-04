n = int(input())

arr = [0, 1]
res = '0 1 '

for i in range(2, n):
    arr.append(((arr[i - 1]) + (arr[i - 2])))
    if i == n -1:
        res += str((arr[i - 1]) + (arr[i - 2])) + ''
    else:
        res += str((arr[i - 1]) + (arr[i - 2])) + ' '
               
print(res)