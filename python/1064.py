count = 0
sum = 0

for x in range(6):
    number = float(input())
    if number > 0: 
        count += 1
        sum += number
        
print(f'{count} valores positivos')
print(f'{(sum / count):.1f}')