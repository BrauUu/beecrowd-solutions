def fat(n):
    if n == 1:
        return 1
    return n * fat(n-1)

n = int(input())
count = 0
x = 0

for i in range(1, 10):
    v = fat(i)
    if v > n:
        break
    x = i

for i in range(x, 0, -1):
    fatI = fat(i)
    x = int(n / fatI)
    count += x
    n -= x * fatI
    
print(count)

