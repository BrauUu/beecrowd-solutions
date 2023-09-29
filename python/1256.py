n = int(input())

for i in range(n):
    m, c = list(map(int, input().split()))
    l = list(map(int, input().split()))
    
    resL = [[] for _ in range(m)]
    
    for item in l:
        resL[item % m].append(item)
       
    if i > 0:
        print() 
        
    for g in range(m):
        res = f'{g} ->'
        for item in resL[g]:
            res += f' {item} ->'
        
        res += ' \\'
        print(res)