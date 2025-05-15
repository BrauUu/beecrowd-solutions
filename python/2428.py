zones = list(map(int, input().split()))
zones.sort()

a1 = zones.pop(0)
flag = False
divisors = []
for i in range(1, a1//2+1, 1):
    if a1 % i == 0:
        divisors.append(i)
divisors.append(a1)

for divisor in divisors:
    newZones = zones.copy()
    newDivisor = divisor
    otherDivisor = a1 // divisor
    i = 0
    j = 1
    while i < len(newZones) >= 1 :
        zone = newZones[i]
        if zone % newDivisor == 0:
            newDivisor = zone // newDivisor
            newZones.pop(i)
            i = 0
            if len(newZones) == 0 and newDivisor != otherDivisor:
                newZones = zones.copy()
                newDivisor = divisor
                i = j
                j += 1
            continue
        i += 1
    if len(newZones) == 0 :
        flag = True     
        break

print('S' if flag else 'N')