while True:
    try:
        num = float(input())
        cutOff = float(input())
        
        if int(num) + cutOff < num:
            print(int(num + 1))
        else:
            print(int(num))
    except:
        break