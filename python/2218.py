l = [1]
sum = 2
for i in range(2, 32001):
    l.append(sum)
    sum += i

t = int(input())

for _ in range(t):
    n = int(input())
    print(l[n])    