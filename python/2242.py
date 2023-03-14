y = input()

x = ''

for i in range(len(y)):
    if y[i] == 'a' or y[i] == 'e' or y[i] == 'i' or y[i] == 'o' or y[i] == 'u':
        x += y[i]

part1 = x[:int(len(x)/2)]
part2 = x[int(len(x)/2+0.99):]
part2Reversed = ''

for i in range(len(part2), 0, -1):
    part2Reversed += part2[i - 1]

if part1 == part2Reversed:
    print('S')
else:
    print('N')