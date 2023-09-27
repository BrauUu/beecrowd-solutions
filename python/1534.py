while True:
    try:
        n = int(input())
        j = n - 1
        for i in range(n):
            res = ''
            res += '3' * (i if i < j else j)
            res += ('1' if i < j else '2') 
            res += '3' * (j - i - 1 if i < j else i - j - 1)
            res += '' if n % 2 == 1 and i == int(n / 2) else ('2' if j > i else '1') 
            res += '3' * ((n - 1)- j if j > i else (n - 1) - i)
            print(res)
            j -= 1
    except:
        break