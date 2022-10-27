n = int(input())

x = input().split()

multiple2Count = 0
multiple3Count = 0
multiple4Count = 0
multiple5Count = 0

for i in range(n):
    y = int(x[i])
    if y % 2 == 0:
        multiple2Count += 1
    if y % 3 == 0:
        multiple3Count += 1
    if y % 4 == 0:
        multiple4Count += 1
    if y % 5 == 0:
        multiple5Count += 1
        
print(f'{multiple2Count} Multiplo(s) de 2')
print(f'{multiple3Count} Multiplo(s) de 3')
print(f'{multiple4Count} Multiplo(s) de 4')
print(f'{multiple5Count} Multiplo(s) de 5')