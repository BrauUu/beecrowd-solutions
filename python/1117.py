grade1 = 0
grade2 = 0

while True:
    grade1 = float(input())
    if grade1 >= 0 and grade1 <= 10:
        break
    else:
        print('nota invalida')
        continue
    
    
while True:
    grade2 = float(input())
    if grade2 >= 0 and grade2 <= 10:
        break
    else:
        print('nota invalida')
        continue
    
print(f'media = {((grade1 + grade2) / 2):.2f}')
    