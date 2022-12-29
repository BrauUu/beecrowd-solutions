n = int(input())

count = 0

for i in range(n):
    x = int(input())
    if x != 1:
        count += 1
        
print(count)