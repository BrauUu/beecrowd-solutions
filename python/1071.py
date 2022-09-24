x = int(input())
y = int(input())

sum = 0

if x > y:
    greater = x
    lower = y
else:
    greater = y
    lower = x

for i in range(lower + 1, greater):
    if i % 2 == 1:
        sum += i
        
print(sum)