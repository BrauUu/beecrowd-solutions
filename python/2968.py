from math import ceil

laps, signs = list(map(int,input().split()))

totalSigns = signs * laps
each10PercentSignsCount = totalSigns / 10
signsCount = each10PercentSignsCount

res = ''
for i in range(9):
    res += str(ceil(signsCount)) + ' '
    signsCount += each10PercentSignsCount
    
print(res.strip())