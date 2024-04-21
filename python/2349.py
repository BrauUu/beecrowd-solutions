n, c, s = list(map(int, input().split()))
cl = list(map(int, input().split()))
ast = 1
count = 0
for command in cl:
    if ast == s:
        count += 1
    ast += command
    if ast > n:
        ast = 1
    elif ast < 1:
        ast = n
if ast == s:
    count += 1
print(count)