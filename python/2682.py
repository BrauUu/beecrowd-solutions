v = 0
flag = False
res = 0
while True:
    try:
        x = int(input())
        if x <= v and flag == False:
            flag = True
            res = v + 1
        else:
            v = x
            if flag == False:
                res = x + 1
    except:
        print(res)
        break