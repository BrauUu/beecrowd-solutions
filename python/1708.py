x, y = list(map(int, input().split()))

i = 1
count = 1
while True:
    if x * (i + 1) <= y * i:
        count += 1
        print(count)
        break
    i += 1
    count += 1