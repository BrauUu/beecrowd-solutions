while True:
    try:
        s = input()
        
        if s == '':
            break

        sum = 0
        count = 1
        
        if len(s) <= 3:
            for i in range(len(s) - 1, -1, -1):
                sum += (ord(s[i]) - 64 ) * count
                count *= 26
            
        print(sum if sum <= 16384 and sum > 0 else 'Essa coluna nao existe Tobias!')
            
    except:
        break