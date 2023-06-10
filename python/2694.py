n = int(input())

for i in range(n):
    x = input()
    temp = ''
    sum = 0
    for j in range(len(x)):
        item = x[j]
        if ord(item) >= 48 and ord(item) <= 57:
            temp += item
        if ord(item) < 48 or ord(item) > 57 or j == len(x) - 1:
            if len(temp) > 0:
                sum += int(temp)
            temp = ''
    print(sum)