from math import ceil

laps, signs = input().split()

totalSigns = int(signs) * int(laps)
signsCountTenPercente = totalSigns / 100 * 10
signsCount = signsCountTenPercente

res = ''
i = 0
while i < 9:
    res += str(ceil(signsCount)) + ' '
    signsCount += signsCountTenPercente
    i += 1
    
print(res.strip())


