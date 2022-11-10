n = int(input())

cameras = []

for i in range (n + 1):
    cameras.append(input().split())
   
for i in range(n):
    res = ''
    for g in range(n):
        count = 0
        if int(cameras[i][g]) == 1:
            count += 1
        if int(cameras[i][g + 1]) == 1:
            count += 1
        if int(cameras[i + 1][g]) == 1:
            count += 1
        if int(cameras[i + 1][g + 1]) == 1:
            count += 1
        if count >= 2:
            res += 'S'
        else:
            res += 'U'
    print(res)
