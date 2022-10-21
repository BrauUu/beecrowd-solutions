x = input().split()

s = int(x[0])
t = int(x[1])
f = int(x[2])

hd = s + t + f

if hd >= 24:
    hd -= 24
elif hd < 0:
    hd = 24 + hd

print(hd)
