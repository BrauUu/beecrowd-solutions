n = int(input())

s = 0
l = list(map(int, input().split()))

for item in l:
    s += (item // 3) * 3
    
print(s)