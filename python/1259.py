n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))
    
evenArr = [x for x in arr if x % 2 == 0]
oddArr = [x for x in arr if x % 2 == 1]

evenArr.sort()
oddArr.sort(reverse=True)

print('-----------')
for x in evenArr:
    print(x)
    
for x in oddArr:
    print(x)