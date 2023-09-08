l = input()
t = input().split()
lenT = len(t)
count = 0

for w in t:
    if w.count(l) >= 1:
        count += 1

print(f'{(count*100/lenT):.1f}')