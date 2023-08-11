l = []
while True:
    try:
        x = input()
        if x == '':
            raise
        l.append(x)
    except:
        l = sorted(l, key=lambda x : x.lower())
        print(l[-1])
        break