sides = input().split()

intSides = []

for i in range(len(sides)):
    intSides.append(int(sides[i]))
    
intSides.sort()

if intSides[2] < intSides[1] + intSides[0] or intSides[1] + intSides[2] > intSides[3]:
    print('S')
else:
    print('N')