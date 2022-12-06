r1, r2, r3 = input().split()
r1 = int(r1)
r2 = int(r2)
r3 = int(r3)

r1c, r2c, r3c = input().split()
r1c = int(r1c)
r2c = int(r2c)
r3c = int(r3c)

count = 0

if r1c > r1:
    count += r1c - r1
if r2c > r2:
    count += r2c - r2
if r3c > r3:
    count += r3c - r3
    
print(count)