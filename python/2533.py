while True:
    try:
        x = int(input())

        ira = 0

        for i in range(x):
            n, c = input().split()
            
            ira += (int(n) * int(c))/(int(c) * 100)
            
        print(f'{(ira / x):.4f}')
    except:
        break