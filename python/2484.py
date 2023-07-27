while True:
    try:
        x = input()
        xCopy = x
        spaces = 0
        for _ in range(len(x)):
            xCopyLen = len(xCopy)
            res = ''
            for char in xCopy:
                res += char + ' '
            res = spaces * ' ' + res.strip()
            print(res)
            xCopy = xCopy[:-1]
            spaces += 1
        print()
    except:
        break