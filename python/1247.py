from math import sqrt

while True:
    try:
        d, vf, vg = list(map(int, input().split()))
        fTime = 12 / vf
        gTime = sqrt(pow(12, 2) + pow(d, 2)) / vg
        if gTime <= fTime:
            print('S')
        else:
            print('N')
    except:
        break