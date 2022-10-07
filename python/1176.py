n = int(input())

arr = [0, 1]

for i in range(2, 61):
    arr.append(arr[i - 1] + arr[i - 2])

for i in range(n):
    x = int(input())
    print(f'Fib({x}) = {arr[x]}')
    