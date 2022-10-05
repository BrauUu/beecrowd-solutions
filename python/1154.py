count = 0
sum = 0
while True:
    age = int(input())
    if age < 0:
        break
    count += 1
    sum += age
    
print(f'{(sum / count):.2f}')