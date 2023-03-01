n = int(input())

for i in range(n):
    x = input()

    count = 0
    countLT = 0
    countGT = 0

    firstLT = x.find('<')
    lastGT = x.rfind('>')

    if firstLT != -1 and lastGT != -1:
        for g in range(firstLT, lastGT + 1):
            if x[g] == '<':
                countLT += 1
            elif x[g] == '>' and countLT > 0:
                countGT += 1

            if countLT >= 1 and countGT >= 1:
                countLT -= 1
                countGT -= 1
                count += 1
    print(str(count))
