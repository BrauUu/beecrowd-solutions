n = int(input())

names = []
countPos = 0
countNeg = 0

for i in range(n):
    signal, name = input().split()
    
    names.append(name)
    
    if signal == '+':
        countPos += 1
    elif signal == '-':
        countNeg += 1
        
names.sort()
        
for g in range(n):
    print(names[g])
    
print(f'Se comportaram: {countPos} | Nao se comportaram: {countNeg}')