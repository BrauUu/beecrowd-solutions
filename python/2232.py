t = int(input())

for i in range(t):
    n = int(input())
    
    sum = 0
    for g in range(n):
        sum += pow(2, g)
        
    print(sum)