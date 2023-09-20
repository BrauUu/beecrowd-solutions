t = int(input())

for i in range(t):
    m, n = list(map(int, input().split()))
    dic = {}
    for g in range(m):
        jp = input()
        pt = input()
        dic.update({jp : pt})
        
    for g in range(n):
        res = ''
        x = list(input().split())
        for w in x:
            res += (dic.get(w) or w) + ' '
    
        print(res.strip())
    print()