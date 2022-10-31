while True:
    try:
        x = input().split()
        month = int(x[0])
        day = int(x[1])

        if len(x) < 1:
            break

        daysLeft = 0

        while month < 12:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
                daysLeft += 31
            if month == 4 or month == 6 or month == 9 or month == 11:
                daysLeft += 30
            if month == 2:
                daysLeft += 29

            month += 1

        daysLeft -= day
        daysLeft += 25

        if daysLeft == 0:
            print('E natal!')
        elif daysLeft == 1:
            print('E vespera de natal!')
        elif daysLeft < 0:
            print('Ja passou!')
        else:
            print(f'Faltam {daysLeft} dias para o natal!')
    except:
        break
