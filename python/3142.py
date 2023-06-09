while True:
    try:
        s = input()

        res = 0
        count = 1
        
        if len(s) <= 3:
            for i in range(len(s) - 1, -1, -1):
                res += (ord(s[i]) - 64 ) * count
                count *= 26
            
        print(res if res <= 16384 and res > 0 else 'Essa coluna nao existe Tobias!')
            
    except:
        break