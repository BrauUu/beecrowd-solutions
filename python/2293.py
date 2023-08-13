n, m = list(map(int, input().split()))

eachRowSum = []
eachCollumnSum = [0 for i in range(m)]

for i in range(n):
    rowSum = 0
    row = list(map(int, input().split()))
    for g in range(len(row)):
        item = row[g]
        rowSum += item
        eachCollumnSum[g] += item
    eachRowSum.append(rowSum)
    
eachRowSum.extend(eachCollumnSum)
print(sorted(eachRowSum)[-1])
        
        