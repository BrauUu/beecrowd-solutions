def listToString(listP):
    res = ''
    for item in listP:
        res += item + ' '
        
    return res.strip()

j = 0

while True:
    n = int(input())
    
    if n == 0:
        break
    
    arr = []
    largest = 0
    
    for i in range(n):
        x = input().split()
        x = listToString(x)
        arr.append(x)
        if len(x) > largest:
            largest = len(x)
            
    if j != 0:    
        print()
        
    j += 1
            
    for i in range(n):
        print(arr[i].rjust(largest, ' '))
    
            
    
        
   