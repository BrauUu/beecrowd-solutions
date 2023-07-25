i = 0
while True:
    try:
        year = int(input())
        
        flagLeap = False
        flagHuluculu = False
        flagBulukulu = False
        
        if i > 0:
            print()
        i += 1
        
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            print('This is leap year.')
            flagLeap = True
        if year % 15 == 0:
            print('This is huluculu festival year.')
            flagHuluculu = True
        if year % 55 == 0 and flagLeap:
            print('This is bulukulu festival year.')
            flagBulukulu = True
        if flagLeap == flagHuluculu == flagBulukulu == False:
            print('This is an ordinary year.')      
    except:
        break        