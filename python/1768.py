while True:
    try:
        x = int(input()) 
       
        for i in range(1, x + 1, 2):
           y = x - i
           print(' ' * int(y / 2) + '*' * i)
           
        print(' ' * int(x / 2) + '*')
        print(' ' * int((x - 3)/ 2) + '***')
        print()
    except:
        break