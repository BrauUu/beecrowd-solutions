from gettext import find


c = int(input())

for i in range(c):
    galopeira = input()
    
    galopeira.find('e')
    galopeira.rfind('e')
    
    time = 0.08 + (0.01 * (galopeira.rfind('e') - galopeira.find('e') + 1))
    
    print(f'{time:.2f}')