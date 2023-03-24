n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    x = arr.pop(0)
    arr.sort()
    print(f'Case {i+1}: {arr[int(x/2)]}')