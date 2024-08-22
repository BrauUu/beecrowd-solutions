l = [1]
for i in range(4, 10**5+1):
    v = (i*l[i-4]) % 1000000009
    l.append(v)
while True:
    n = int(input())
    if n == 0:
        break
    print(l[n-3])