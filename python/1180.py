n = int(input())

arr = input().split()
lower = int(arr[0])
pos = 0

for i in range(n):
    arr[i] = int(arr[i])
    if arr[i] < lower:
        lower = arr[i]
        pos = i
        
print(f'Menor valor: {lower}')
print(f'Posicao: {pos}')
    