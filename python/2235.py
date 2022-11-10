x1, x2, x3 = input().split()
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)

arr = [x1, x2, x3]
arr.sort()


if arr[0] == arr[1] or arr[1] == arr[2]:
    print('S')
elif arr[0] + arr[1] == arr[2]:
    print('S')
else:
    print('N')