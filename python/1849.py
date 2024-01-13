ld, cd, lv, cv = list(map(int, input().split()))
if ld < cd:
    temp1 = lv if lv < cv else cv
    temp2 = lv if lv > cv else cv
    x = ld + temp1
    y = cd if cd < temp2 else temp2
else:
    temp1 = lv if lv < cv else cv
    temp2 = lv if lv > cv else cv
    x = cd + temp1
    y = ld if ld < temp2 else temp2
    
v = x**2 if x < y else y**2
print(v)