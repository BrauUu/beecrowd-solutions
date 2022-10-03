alcoholCount = 0
gasCount = 0
dieselCount = 0

while True:
    x = int(input())
    
    if x == 1:
        alcoholCount += 1
    if x == 2:
        gasCount += 1
    if x == 3:
        dieselCount += 1
    if x == 4:
        break

print('MUITO OBRIGADO')
print(f'Alcool: {alcoholCount}')
print(f'Gasolina: {gasCount}')
print(f'Diesel: {dieselCount}')