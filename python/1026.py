while True:
    try:
        x , y = input().split()
        x = bin(int(x))[2:]
        y = bin(int(y))[2:]

        sum = ''
        actual = ''
        carry = ''


        x = (len(y) - len(x)) * '0' + x if len(y) >= len(x) else x
        y = (len(x) - len(y)) * '0' + y if len(x) >= len(y) else x

        for i in range(len(x) - 1, -1, -1):
            if x[i] == y[i] == carry == '1':
                carry = '0'
                actual = '1'
            elif x[i] == carry == '1' or x[i] == y[i] == '1' or carry == y[i] == '1':
                carry = '0'
                actual = '0'
            elif x[i] == '1' or y[i] == '1' or carry == '1':
                carry = '0'
                actual = '1'
            else:
                carry = '0'
                actual = '0'
            sum = actual + sum
            
        if carry == '1':
            sum = carry + sum

        
        print(int('0b' + sum, base=2))
    except:
        break