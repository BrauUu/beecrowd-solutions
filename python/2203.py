while True:
    try:
        inputs = input().split()

        xF = int(inputs[0])
        yF = int(inputs[1])
        xI = int(inputs[2])
        yI = int(inputs[3])
        vI = int(inputs[4])
        r1 = int(inputs[5])
        r2 = int(inputs[6])

        distance = abs((xI + yI) - (xF + yF))

        if  r1 + r2 >= distance + (vI * 1.5):
            print('Y')
        else:
            print('N')
    except:
        break