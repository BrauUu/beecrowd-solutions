n = int(input())

arr = []

g = int(input())

for i in range(g):
    x = int(input())
    
    flag = False
    
    for el in arr:
        if el == x:
            flag = True
            
    if flag == False:
        arr.append(x)
    
    
print(n - len(arr))