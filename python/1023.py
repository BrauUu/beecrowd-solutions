from sys import stdout, stdin

def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

j = 0

while True:
    j += 1
    n = int(stdin.readline())
    
    if n == 0:
        break
    
    obj = {}
    arr = []
    totalQty = 0
    totalNb = 0
    
    for i in range(n):
        nb, qty = map(int, stdin.readline().split())
        
        totalQty += qty
        totalNb += nb
        
        key = int(qty/nb)
        
        v = obj.get(key)
        
        if v == None:
            obj[key] = nb 
            arr.append(key)
        else:
            obj[key] =  v + nb
    
    quick_sort(arr, 0, len(arr) - 1)
     
    res = ''
    for x in arr:
        res += f'{obj[x]}-{x} '
    
    stdout.write(f'Cidade# {j}:\n' if j == 1 else f'\nCidade# {j}:\n')
    stdout.write(f'{res.strip()}\n')
    stdout.write(f'Consumo medio: {totalQty / totalNb - 0.0049:.2f} m3.\n')