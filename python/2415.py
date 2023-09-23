n = int(input())

l = list(map(int, input().split()))

maxSeq = 0
actualSeq = 0
numSeq = 0
previousNumSeq = 0

for i in range(n):
    numSeq = l[i]
    if i == 0:
        actualSeq += 1
    elif numSeq == previousNumSeq:
        actualSeq += 1
    else:
        if actualSeq > maxSeq:
            maxSeq = actualSeq
        actualSeq = 1
    previousNumSeq = l[i]
    
if actualSeq > maxSeq:
    maxSeq = actualSeq
    
print(maxSeq)