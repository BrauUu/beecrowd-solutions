from sys import stdout, stdin

n, m = list(map(int, stdin.readline().split()))
rules = {}
b = 'A'

for _ in range(m):
    b1, b2 = stdin.readline().split()
    rules[b1] = b2

for _ in range(n):
    newB = ''
    while len(b) > 0:
        char = b[0]
        endPos = b.find('B' if char == 'A' else 'A')
        endPos = endPos if endPos != -1 else len(b)
        key = b[0: endPos]
        newValue = rules[key]
        newB += newValue
        acc = endPos
        b = b[endPos:]
    b = newB

stdout.write(f'{b.count("A")} {b.count("B")}\n')