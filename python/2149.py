def philBonaci(x, y, i, arr):
    if i == 0:
        return
    z = 0
    if i % 2 == 1:
        z = x + y
    else:
        z = x * y
    arr.append(z)
    philBonaci(y, z, i-1, arr)
    
arr = [0,1]
philBonaci(0, 1, 15, arr)

while True:
    try:
        n = int(input())
        print(arr[n-1])
    except:
        break
