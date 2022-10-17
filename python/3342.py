x = int(input())

order = True

whiteCount = 0
blackCount = 0

for i in range(x):
    for j in range(1, x + 1):
        if order == True:
            if j % 2 == 1:
                whiteCount += 1
            else:
                blackCount += 1
        else:
            if j % 2 == 1:
                blackCount += 1
            else:
                whiteCount += 1
    order = -order
                
print(f'{whiteCount} casas brancas e {blackCount} casas pretas')