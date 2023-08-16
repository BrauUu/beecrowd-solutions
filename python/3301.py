h, z, l = list(map(int, input().split()))

if (h > z or h > l) and (h < z or h < l):
    print('huguinho')

elif(l > z or l > h) and (l < z or l < h):
    print('luisinho')

elif(z > h or z > l) and (z < h or z < l):
    print('zezinho')