while True:
    try:
        n = int(input())
        
        x2 = 0
        x3 = n - 1
        
        for i in range(n):
            line = ''
            for g in range(n):
                if i == int(n/2) and g == int(n/2):
                    line += '4'
                elif (i >= int(n/3) and i < (n - int(n/3)) ) and (g >= int(n/3) and g < (n - int(n/3))):
                    line += '1'
                elif g == x2:
                    line += '2'
                elif g == x3:
                    line += '3'
                else:
                    line += '0'
            x2 += 1                     
            x3 -= 1
            print(line)
        print()
    except:
        break