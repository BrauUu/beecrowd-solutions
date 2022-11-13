grade = int(input())

if grade == 0:
    print('E')
elif grade >= 1 and grade <= 35:
    print('D')
elif grade >= 36 and grade <= 60:
    print('C')
elif grade >= 61 and grade <= 85:
    print('B')
elif grade >= 86 and grade <= 100:
    print('A')