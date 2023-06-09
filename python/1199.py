while True:
    x = input()
    if x.startswith('0x') == True:
        print(int(x, base=16))
    else:
        if int(x) < 0:
            break
        print('0x' + hex(int(x))[2:].upper())