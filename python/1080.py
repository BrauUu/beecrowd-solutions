arr = []

for i in range(100):
    arr.append(int(input()))
    
bigger = 0
pos = 0
for i in range(len(arr)):
    if arr[i] > bigger:
        bigger = arr[i]
        pos = i + 1
        
print(bigger)
print(pos)
        