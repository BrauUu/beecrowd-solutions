n, q, l = list(map(float, input().split()))

names = input().split()

qTimes10 = int(q * 10)
lTimes10 = int(l * 10)

numOfCuias = qTimes10 // lTimes10
ind = int(numOfCuias - (numOfCuias // n * n))

temp = q - (numOfCuias*l)
rest = temp if temp > 0 else l

ind = ind - 1 if temp == 0 else ind

print(f'{names[ind]} {rest:.1f}')