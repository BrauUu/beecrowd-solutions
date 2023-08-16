f = ''
m = []
l = ''

for i in range(4):
    x = input()
    f += x[0]
    for g in range(1, len(x[0:-1])):
        if i == 0:
            m.append(x[g])
        else: 
            m[g - 1] += x[g]
    l += x[-1]
    
res = ''
    
for i in range(len(m)):
    res += chr((int(f) * int(m[i]) + int(l)) % 257)
    
print(res)
    
