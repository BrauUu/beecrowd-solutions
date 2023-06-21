n, k = list(map(int, input().split()))

namesList = []

for i in range(n):
    namesList.append(input())
    
namesList.sort()
print(namesList[k - 1])