n = int(input())

for i in range(n):
    xArr = input().split()
    res = ''
    for x in xArr:
        res += x[0] if len(x) > 0 else ''
        
    print(res)