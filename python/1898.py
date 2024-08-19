from math import floor

x1 = input()
x2 = input()

temp = ''
cpf = ''
v = 0

for char in x1:
    if len(cpf) < 11:
        if char.isnumeric():
            cpf += char
        continue
    if char.isnumeric() or char == '.':
        temp += char

v = floor(float(temp) * 100)/100
temp = ''

for char in x2:
    if char.isnumeric() or char == '.':
        temp += char

v += floor(float(temp) * 100)/100

print(f'cpf {cpf}')
n = f'{v:.2f}'
print(f'{n[:17 if len(str(n)) > 17 else len(str(n))]}')