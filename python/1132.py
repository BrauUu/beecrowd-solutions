x = int(input())
y = int(input())

if x > y:
    w = x
    z = y
else:
    w = y
    z = x

sum = 0

for i in range(z,w+1):
    if i % 13 == 0:
        continue
    else:
        sum += i

print(sum)