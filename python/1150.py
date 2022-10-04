from re import I


x = int(input())
z = 0

while True:
    z = int(input())
    if z > x:
        break

sum = x
i = 1
while sum <= z:
    sum += x + i 
    i += 1
    
print(i)