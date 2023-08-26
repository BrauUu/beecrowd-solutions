while True:
    try:
        n = int(input())
        
        countEPR = 0
        countEHD = 0
        countIntruder = 0
        
        for i in range(n):
            cod, course = input().split()
            if course == 'EPR':
                countEPR += 1
            elif course == 'EHD':
                countEHD += 1
            else:
                countIntruder += 1
        
        print(f'EPR: {countEPR}')
        print(f'EHD: {countEHD}')
        print(f'INTRUSOS: {countIntruder}')
    except:
        break
        