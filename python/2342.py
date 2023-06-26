n = int(input())

n1, operator, n2 = input().split()
res = 0

if operator == '*' or operator == '+':
    res = eval(f'{int(n1)} {operator} {int(n2)}')

print('OK' if res <= n else 'OVERFLOW')