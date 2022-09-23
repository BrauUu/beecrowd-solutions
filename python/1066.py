oddCount = 0
evenCount = 0
posCount = 0
negCount = 0

for i in range(5):
    num = (int(input()))
    if num % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
    if num > 0:
        posCount += 1
    elif num < 0:
        negCount += 1
        
print(evenCount, 'valor(es) par(es)')
print(oddCount, 'valor(es) impar(es)')
print(posCount, 'valor(es) positivo(s)')
print(negCount, 'valor(es) negativo(s)')


