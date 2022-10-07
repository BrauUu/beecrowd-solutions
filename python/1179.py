oddArray = []
evenArray= []

def showArr(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            print(f'par[{i}] = {arr[i]}')
        elif arr[i] % 2 == 1:
            print(f'impar[{i}] = {arr[i]}')

for i in range(15):
    x = int(input())
    if x % 2 == 0:
        evenArray.append(x)
    elif x % 2 == 1:
        oddArray.append(x)
        
    if len(evenArray) == 5:
        showArr(evenArray)
        evenArray.clear()
    elif len(oddArray) == 5:
        showArr(oddArray)
        oddArray.clear()
        
showArr(oddArray)
showArr(evenArray)