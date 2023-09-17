n = int(input())

for i in range(n):
    x = input()
    y = input()
    res = ''
    for g in range(0, len(x), 2):
        res += x[g:g+2] + y[g:g+2]
    
    print(res)