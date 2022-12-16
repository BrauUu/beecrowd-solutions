a = int(input())
b = int(input())
c = int(input())

aNeg = '-' + '0' * (10 - len(str(a)))
aPos =  '0' * (10 - len(str(a)))

print(f'A = {a}, B = {b}, C = {c}')
print('A = ', ' ' * (10 - len(str(a))), a, ', B = ', ' ' * (10 - len(str(b))), b, ', C = ', ' ' * (10 - len(str(c))), c, sep='')
print('A = ', aNeg + str(a)[1:] if a < 0 else aPos + str(a), ', B = ', '0' * (10 - len(str(b))), b, ', C = ', '0' * (10 - len(str(c))), c, sep='')
print('A = ', a, ' ' * (10 - len(str(a))), ', B = ', b, ' ' * (10 - len(str(b))), ', C = ', c,' ' * (10 - len(str(c))), sep='')