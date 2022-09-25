n = int(input())

def oddOrEven(number):
    if number % 2 == 0:
        return 'EVEN'
    elif number % 2 == 1:
        return 'ODD'
    
for i in range(n):
    number = int(input())
    if number > 0:
        print(oddOrEven(number),'POSITIVE')
    elif number < 0:
        print(oddOrEven(number),'NEGATIVE')
    else:
        print('NULL')
        