sum = 0
count = 0
while True:
    try:
        name = input()
        
        if name == '':
            raise Exception
        
        sum += int(input())
        count += 1
    except:
        print(f'{sum/count:.1f}')
        break