n = int(input())

sum = 0

for i in range(n):
    t, c = input().split()
    
    if t == 'V':
        sum += int(c)
    elif t == 'G':
        sum -= int(c)
        
print("NAO VAI TER CORTE, VAI TER LUTA!" if sum < 0 else "A greve vai parar.")