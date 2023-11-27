n, m = list(map(int, input().split()))
firstV = secondV = thirdV = 0
first = second = third = 0

for i in range(1, n + 1):
    s = sum(list(map(int, input().split())))
    if s < firstV or firstV == 0:
        thirdV = secondV
        third = second
        secondV = firstV
        second = first
        firstV = s
        first = i
    elif s < secondV or secondV == 0:
        thirdV = secondV
        third = second
        secondV = s
        second = i
    elif s < thirdV or thirdV == 0:
        third = i
        thirdV = s

print(first, second, third, sep='\n')