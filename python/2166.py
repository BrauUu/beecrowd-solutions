n = int(input())

def fr(n):
    n -= 1
    if n == 0:
        return 2
    return 2 + 1/fr(n)

num = 1

if n == 0 :
    print(f'{num:.10f}')
else:
    num = num + 1 / fr(n)      
    print(f'{num:.10f}')