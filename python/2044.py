while True:
    n = int(input())
    if n == -1:
        break
    values = list(map(int, input().split()))
    count = 0
    sum = 0
    for value in values:
        sum += value
        if sum % 100 == 0:
            sum = 0
            count +=1
    print(count)