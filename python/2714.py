n = int(input())

for i in range(n):
    x = input()
    ra = x[:2] or ''
    num = x[2:] or ''
    if ra == 'RA' and len(num) == 18:
        print(int(num))
    else:
        print('INVALID DATA')
    