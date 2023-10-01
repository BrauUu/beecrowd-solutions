while True:
    try:
        x = input()
        y = input()

        count = 0
        for item in x:
            count += y.count(item)
            
        print(count)
    except:
        break