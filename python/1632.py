t = int(input())
a = ['A', 'E', 'I', 'S', 'O']
for _ in range(t):
    s = input()
    count = 1
    for l in s:
        if a.count(l.upper()) > 0:
            count *= 3
        else:
            count *= 2
    print(count)