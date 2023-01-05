n = int(input())

for i in range(n):
    h, d, g = input().split()
    h = int(h)
    d = int(d)
    g = int(g)
    
    if h >= 200 and h <= 300:
        if d >= 50:
            if g >= 150:
                print("Sim")
                continue
    print("Nao")