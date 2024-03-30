b = int(input())
g = int(input())

diff = int(g/2) - b

if diff <= 0:
    print('Amelia tem todas bolinhas!')
elif diff > 0:
    print(f'Faltam {diff} bolinha(s)')