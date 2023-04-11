n = int(input())

for i in range(n):
    x, y = list(map(int, input().split()))
    
    res = ''
    mirrorRes = ''
    
    for j in range(x, y+1):
        j = str(j)
        res += j
        reverseJ = ''
        for g in range(len(j) - 1, -1, -1):
            reverseJ += str(j[g])
        mirrorRes = reverseJ + mirrorRes
        
    print(res + mirrorRes)