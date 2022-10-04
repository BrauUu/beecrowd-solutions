arr = input().split()
a = int(arr[0])
n = 0

for i in range(1, len(arr)):
    if int(arr[i]) > 0 and n == 0:
        n = int(arr[i])

sum = 0

for i in range(n - 1, -1, -1):
    sum += a + i
    
print(sum)
    