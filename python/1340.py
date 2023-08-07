while True:
    try: 
        n = int(input())
        data = []
        maxV = 0
        flags = [True, True, True]
        for i in range(n):
            cmd, x = list(map(int, input().split()))
            if cmd == 1:
                if x > maxV: # type: ignore
                    maxV = x
                data.append(x)
            elif cmd == 2:
                if data.count(x) == 0:
                    flags = [False, False, False]
                else:
                    if x != maxV:
                        flags[2] = False
                    if list(reversed(data)).index(x) != 0:
                        flags[0] = False
                    if data.index(x) != 0:
                        flags[1] = False
                    if flags[0] == True:
                       data.pop()
                    else:
                        data.remove(x)
                    if len(data) > 0:
                        maxV = sorted(data)[len(data)-1]
        
        if flags.count(True) > 1:
            print('not sure')
        elif flags.count(True) == 0:
            print('impossible')
        elif flags.count(True) == 1:
            match flags.index(True):
                case 0:
                    print('stack')
                case 1:
                    print('queue')
                case 2:
                    print('priority queue')
    except:     
        break