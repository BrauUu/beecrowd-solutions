n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))
    
count = 0
    
for i in range(n):
    if i == n - 1:
        count += 1
    elif arr[i] != arr[i + 1]:
        count += 1
        
print(count)