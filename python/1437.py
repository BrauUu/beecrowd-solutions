directions = ['N', 'L', 'S', 'O']

while True:
    n = int(input())
    if n == 0:
        break
    x = input()
    pos = 0
    for i in range(len(x)):
        if x[i] == 'D':
            pos = pos + 1 if pos < 3 else 0
        elif x[i] == 'E':
            pos = pos - 1 if pos > 0 else 3
    
    print(directions[pos])

