i = 0

while i <= 2: 
    j = 1 + i
    for x in range(3):
        if i % 1 == 0:
            i = int(i)
        if j % 1 == 0:
            j = int(j)
        print(f'I={i} J={j}')
        j += 1
    i += 0.2
    i = round(i, 2)