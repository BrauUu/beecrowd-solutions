n = int(input())

countDolls = 0
countArch = 0
countMusic = 0
countDesigner = 0

for i in range(n):
    name, sector, hours = input().split()
    
    if sector == 'bonecos':
        countDolls += int(hours)
    elif sector == 'arquitetos':
        countArch += int(hours)
    elif sector == 'musicos':
        countMusic += int(hours)
    elif sector == 'desenhistas':
        countDesigner += int(hours)
        
sum = int(countDolls / 8) + int(countArch / 4) + int(countMusic / 6) + int(countDesigner / 12)
print(sum)