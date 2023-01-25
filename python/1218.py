x = 0
while True:
    try:
        n = int(input())
        
        count = 0
        countM = 0
        countF = 0
        
        shoesSizeAndGender = input().split()
        for i in range(0, len(shoesSizeAndGender), 2):
            if int(shoesSizeAndGender[i]) == n:
                count += 1
                if shoesSizeAndGender[i + 1] == 'M':
                    countM += 1
                elif shoesSizeAndGender[i + 1] == 'F':
                    countF += 1
        if x > 0:
            print()   
        
        x += 1
                 
        print(f'Caso {x}:')
        print(f'Pares Iguais: {count}')
        print(f'F: {countF}')
        print(f'M: {countM}')
        
    except:
        break