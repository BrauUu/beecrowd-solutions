while True:
    x = int(input())
    if x == 0:
        break
    response = ''
    for i in range(1, x + 1):
        if i == x:
            response = response + str(i)
        else:
            response = response + str(i) + ' '
    print(response)