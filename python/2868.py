n = int(input())

for _ in range(n):
    exp = input()
    n1, operator, n2, _, result = exp.split()
    n1 = int(n1)
    n2 = int(n2)
    result = int(result)
    correctResult = 0
    if operator in ['+', '-', 'x', '/']:
        if operator == 'x':
            correctResult = eval(f'{n1} * {n2}')
        else:
            correctResult = eval(f'{n1} {operator} {n2}')
    
    diff = abs(correctResult - result)
    print(f'E{"r" * diff}ou!')