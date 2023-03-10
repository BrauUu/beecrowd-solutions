n = int(input())

x = ''

if n == 1:
    x = '1'
elif n <= 3:
    x = '3'
elif n <= 5:
    x = '5'
elif n <= 10:
    x = '10'
elif n <= 25:
    x = '25'
elif n <= 50:
    x = '50'
elif n <= 100:
    x = '100'
    
print(f'Top {x}')