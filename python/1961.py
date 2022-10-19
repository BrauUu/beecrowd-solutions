p, n = input().split()
p = int(p)
n = int(n)

x = input().split()
lose = False

for i in range(1, n):
    pipeH = int(x[i])
    if pipeH > p and pipeH > int(x[i - 1]) + p:
        print('GAME OVER')
        lose = True
        break
    elif pipeH < int(x[i - 1]) - p:
        print('GAME OVER')
        lose = True
        break

if lose == False:
    print('YOU WIN')
