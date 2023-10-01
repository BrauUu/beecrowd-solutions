sum = 0
count = 0
while True:
    wl, wr, r = list(map(int, input().split()))
    
    if wl == wr == r == 0:
        break
    
    w = (wl + wr) / 2

    m = w * (1 + r/30)
    sum += m
    count += 1
    
    res = ''
    
    if m >= 1 and m < 13:
        res = "Nao vai da nao"
    elif m >= 13 and m < 14:
        res = "E 13"
    elif m >= 14 and m < 40:
        res = "Bora, hora do show! BIIR!"
    elif m >= 40 and m <= 60:
        res = "Ta saindo da jaula o monstro!"
    elif m > 60:
        res = "AQUI E BODYBUILDER!!"
        
    print(res)
       
print()
print("Aqui nois constroi fibra rapaz! Nao e agua com musculo!" if (sum/count) > 40 else '')    