n = int(input())

arr = input().split()
res = ''

for item in arr:
    if len(item) == 3:
        if item.startswith('OB') or item.startswith("UR"):
            item = item[0:2] + "I"
    res += item + ' '

print(res.strip())