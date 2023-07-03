n = int(input())
count = 0

for i in range(n):
    l, c = list(map(int, input().split()))
    if l > c:
        count += c

print(count)
    
    
    