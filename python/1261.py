n, m = list(map(int, input().split()))

hayPoints = {}

for i in range(n):
    x, v = input().split()
    
    hayPoints.update({x : int(v)})
    
for i in range(m):
    desc = ''
    while True:
        x = input()
        if x == '.':
            break
        desc += x + ' '
    
    sum = 0
        
    for item in hayPoints:
        sum += desc.count(item) * hayPoints.get(item, 0)
        
    print(sum)