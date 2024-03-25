n = int(input())

employees = [i for i in range(1, n+1)]

q = int(input())

for i in range(q):
    e, *x = list(map(int, input().split()))

    if e == 1:
        temp = employees.index(x[0])
        employees[employees.index(x[1])] = x[0]
        employees[temp] = x[1]
    elif e == 2:
        flag = False
        ind = x[0] - 1
        count = 0
        while flag == False:
            employee = employees[ind]
            if employee == x[0]:
                flag = True
            else:
                ind = employee - 1
                count += 1
        print(count)