n = int(input())

s = 'FACE'
count = 0

for i in range(n):
    x = input()
    x = x.replace(' ', '')
    reversedX = x[::-1]
    latestWord = s[-4:]
    if latestWord == reversedX:
        count += 1
        s = s[:-4]
    else:
        s += x
    if len(s) == 0:
        s = 'FACE'
print(count)
    