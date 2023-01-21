while True:
    try:
        x, y, m = input().split()
        x = int(x)
        y = int(y)
        m = int(m)
        
        
        for i in range(m):
            xi, yi = input().split()
            xi = int(xi)
            yi = int(yi)
            
            if xi * yi <= x * y:
                if xi <= x:
                    if yi <= y:
                        print("Sim")
                        continue
                if xi <= y:
                    if yi <= x:
                        print("Sim")
                        continue
                    
            print("Nao")
    except:
        break
        