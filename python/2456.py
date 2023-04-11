arr = list(map(int, input().split()))
cArr = arr.copy()
dArr = arr.copy()

cArr.sort()
dArr.sort(reverse=True)

flagC = True
flagD = True

for i in range(len(arr)):
    if arr[i] != cArr[i]:
        flagC = False
    if arr[i] != dArr[i]:
        flagD = False
        
if flagC == True:
    print('C')
elif flagD == True:
    print('D')
else:
    print('N')