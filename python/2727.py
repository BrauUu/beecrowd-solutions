while True:
    try:
        n = int(input())
        
        for i in range(n):
            x = input()
            x = x.split()
            
            v = 96 + len(x[0]) + ((len(x) - 1) * 3)
            print(chr(v))
    except:
        break