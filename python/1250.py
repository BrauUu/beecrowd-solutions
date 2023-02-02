n = int(input())

for i in range(n) :
    
    t = int(input())
    
    x = list(map(int, input().split()))
    y = input()
    
    hit = 0
    
    for j in range(t):
        if x[j] > 2 and y[j] == 'J' or x[j] <= 2 and y[j] == 'S':
            hit += 1
            
    print(hit)
    