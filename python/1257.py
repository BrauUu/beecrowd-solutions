n = int(input())

for i in range(n):
    sum = 0
    l = int(input())
    for g in range(l):
        line = input()
        for h in range(len(line)):
            sum += (ord(line[h]) - 65) + g + h
        
    print(sum)