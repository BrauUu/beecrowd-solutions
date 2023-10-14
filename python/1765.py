while True:
    t = int(input())
    
    if t == 0:
        break
    
    for i in range(t):
        q, b1, b2 = input().split()
        q = int(q)
        b1 = float(b1)
        b2 = float(b2)
        
        t = ((b1 + b2) * 5 / 2) * q
        
        print(f'Size #{i + 1}:')
        print(f'Ice Cream Used: {t:.2f} cm2')
        
    print()