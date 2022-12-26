n = int(input())

arr = []

for i in range(n):
    arr.append(input().split())
    
countHome = 0
boughtHome = 0
countOffice = 0
boughtOffice = 0

for i in range(n):
    if arr[i][0] == 'chuva':
        if countHome > 0:
            countHome -= 1
            countOffice += 1
        else:
            boughtHome += 1
            countOffice += 1
    if arr[i][1] == 'chuva':
        if countOffice > 0:
            countOffice -= 1
            countHome += 1
        else:
            boughtOffice += 1
            countHome += 1
            
print(boughtHome, boughtOffice)