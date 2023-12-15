from sys import stdout, stdin

while True:
    try:
        s = str(stdin.readline())[:-1]
        
        if s == '':
            break

        sum = 0
        count = 1
        
        if len(s) <= 3:
            for i in range(len(s) - 1, -1, -1):
                sum += (ord(s[i]) - 64 ) * count
                count *= 26
                
        if sum <= 16384 and sum > 0: 
            stdout.write(f'{sum}\n')
        else:
            stdout.write('Essa coluna nao existe Tobias!\n')
            
    except:
        break