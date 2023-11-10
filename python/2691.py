n = int(input())

for _ in range(n):
    n1, n2 = list(map(int, input().split('x')))

    flag = False

    if n1 == n2:
        flag = True
        
    for g in range(5, 11):
        res = f'{n1} x {g} = {n1 * g}'
        if flag == False:
            res += f' && {n2} x {g} = {n2 * g}'
        print(res)