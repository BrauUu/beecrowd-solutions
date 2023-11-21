while True:
    try:
        hours, minutes = list(map(int, input().split(':')))
        bHours = bin(hours)[2:]
        bMinutes = bin(minutes)[2:]
        
        print(f' {"_" * 44}')
        print(f'|{" " * 44}|')
        print(f'|{" " * 4}{"_" * 36}{" " * 4}|_')
        print(f'|   |{" " * 36}|   |_)')
        print(f'|   |   8         4         2         1  |   |')
        print(f'|   |{" " * 36}|   |')
        print(f'|   |   {"o" if len(bHours) >= 4 and bHours[-4] == "1" else " "}         {"o" if len(bHours) >= 3 and bHours[-3] == "1" else " "}         {"o" if len(bHours) >= 2 and bHours[-2] == "1" else " "}         {"o" if len(bHours) >= 1 and bHours[-1] == "1" else " "}  |   |')
        print(f'|   |{" " * 36}|   |')
        print(f'|   |{" " * 36}|   |')
        print(f'|   |   {"o" if len(bMinutes) >= 6 and bMinutes[-6] == "1" else " "}     {"o" if len(bMinutes) >= 5 and bMinutes[-5] == "1" else " "}     {"o" if len(bMinutes) >= 4 and bMinutes[-4] == "1" else " "}     {"o" if len(bMinutes) >= 3 and bMinutes[-3] == "1" else " "}     {"o" if len(bMinutes) >= 2 and bMinutes[-2] == "1" else " "}     {"o" if len(bMinutes) >= 1 and bMinutes[-1] == "1" else " "}  |   |')
        print(f'|   |{" " * 36}|   |')
        print(f'|   |   32    16    8     4     2     1  |   |_')
        print(f'|   |{"_" * 36}|   |_)')
        print(f'|{" " * 44}|')
        print(f'|{"_" * 44}|')
        print()
    except:
        break