response = 1
grade1 = -1
grade2 = -1

while response == 1:
    while True:
        grade1 = float(input())
        if grade1 < 0 or grade1 > 10:
            print('nota invalida')
        else:
            break
    while True:
        grade2 = float(input())
        if grade2 < 0 or grade2 > 10:
            print('nota invalida')
        else:
            break
        
    avg = (grade1 + grade2) / 2
    print(f'media = {avg:.2f}')
    while True:
        print('novo calculo (1-sim 2-nao)')
        response = int(input())
        if response == 2 or response == 1:
            break
