n = int(input())

def fr(n):
    n -= 1
    if n == 0:
        return 6
    return 6 + 1/fr(n)

num = 3

if n == 0 :
    print(f'{num:.10f}')
else:
    num = num + 1 / fr(n)      
    print(f'{num:.10f}')