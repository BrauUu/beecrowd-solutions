n = int(input())

numbers = input().split()

if n == 1:
    print(1)
else:
    oldDiff = 0
    count = 0
    for i in range(n - 1):
        diff = int(numbers[i]) - int(numbers[i+1])
        if i != 0 and diff != oldDiff:
            count += 1
            oldDiff = diff
        elif i == 0:
            oldDiff = diff
            count += 1
    print(count)