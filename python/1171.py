n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))
    
arr.sort()
count = 0
x = arr[0]

for i in range(len(arr)):
    if i > 0 and arr[i] != arr[i-1]:
        print(f'{x} aparece {count} vez(es)')
        count = 1
        x = arr[i]
    else:
        count += 1
        
    if i == len(arr) - 1:
        print(f'{x} aparece {count} vez(es)')
