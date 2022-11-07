n = int(input())

values = input().split()
index = 0

for i in range(n - 1):
    if int(values[i]) > int(values[i + 1]):
        index = i + 2
        break
    
print(index)