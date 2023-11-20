def isPrimo(number):
    if number < 2:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    return True

n, m = list(map(int, input().split()))
p1 = p2 = 0

for i in range(n, 1, -1):
    if isPrimo(i):
        p1 = i
        break
    
for i in range(m, 1, -1):
    if isPrimo(i):
        p2 = i
        break
    
print(p1 * p2)