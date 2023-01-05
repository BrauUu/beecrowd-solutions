n = int(input())

carCount = 0
dollCount = 0

for i in range(n):
    name, sex = input().split()
    
    if sex == "F":
        dollCount += 1
    elif sex == "M":
        carCount += 1

print(f'{carCount} carrinhos')
print(f'{dollCount} bonecas')