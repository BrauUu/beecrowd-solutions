while True:
    arr = input().split()
    arr.sort()
    
    n = int(arr[0])
    m = int(arr[1])
    
    if n <= 0 or m <= 0:
        break
    
    seq = ''
    sum = 0
    
    for i in range(n,m + 1):
        seq += str(i) + ' '
        sum += i
        
    print(f'{seq}Sum={sum}')
