n = int(input())

arr = list(map(int, input().split()))

arr.sort()

cont = 0
i = 0
lenArr = len(arr)
while i < lenArr and arr[i] == 0:
    cont += 1
    i += 1
    
if cont > int(lenArr / 2):
    print('Y')
else:
    print('N')