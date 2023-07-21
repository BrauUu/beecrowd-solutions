n, m = list(map(int, input().split()))

count = 0

for i in range(n):
    goalsPerMatch = list(map(int, input().split()))
    
    flag = False
    for g in range(m):
        if goalsPerMatch[g] == 0:
            flag = True
            break
    if flag == False:    
        count += 1
        
print(count)

