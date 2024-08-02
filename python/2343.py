from sys import stdin, stdout

n = int(stdin.readline())
s = set()
flag = False
for _ in range(n):
    x, y = stdin.readline().split()
    q = f'{x} {y}'
    s.add(q)
cond = '0\n' if len(s) == n else '1\n'
stdout.write(cond)