day1, day2, day3 = input().split()
day1 = int(day1)
day2 = int(day2)
day3 = int(day3)

if day1 > day2 and (day2 == day3 or day2 < day3):
    print(':)')
elif day1 < day2 and (day2 == day3 or day2 > day3):
    print(':(')
elif day1 < day2 and day2 < day3 and (day3 - day2 < day2 - day1):
    print(':(')
elif day1 < day2 and day2 < day3 and (day3 - day2 >= day2 - day1):
    print(':)')
elif day1 > day2 and day2 > day3 and (day2 - day3 < day1 - day2):
    print(':)')
elif day1 > day2 and day2 > day3 and (day2 - day3 >= day1 - day2):
    print(':(')
elif day1 == day2:
    if day2 - day3 < 0:
        print(':)')
    else:
        print(':(')