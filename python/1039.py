from math import sqrt

while True:
    try:
        r1, x1, y1, r2, x2, y2 = map(int, input().split())
        
        distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
        print('RICO' if distance + r2 <= r1 else 'MORTO')
        
    except:
        break