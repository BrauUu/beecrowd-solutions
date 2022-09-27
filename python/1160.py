t = int(input())

popA = 0
popB = 0
taxA = 0
taxB = 0

for i in range(t):
    arr = input().split()
    popA = int(arr[0])
    popB = int(arr[1])
    taxA = float(arr[2])
    taxB = float(arr[3])
    years = 0
    while True:
        popA += int(popA * taxA / 100)
        popB += int(popB * taxB / 100)
        years += 1
        
        if years > 100:
            print('Mais de 1 seculo.')
            break
        if popA > popB:
            print(f'{years} anos.')
            break
    
    