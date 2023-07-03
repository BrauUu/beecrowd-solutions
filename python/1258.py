order = ["P", "M", "G"]

y = 1
while True:
    n = int(input())

    if n == 0:
        break

    studentsArr = []

    for i in range(n):
        name = input()
        color, size = input().split()

        student = (name, color, size)

        studentsArr.append(student)
        
    newStudentsArr = sorted(studentsArr, key=lambda x: (x[1], order.index(x[2]), x[0]))

    if y > 1:
        print()
    y += 1
    for student in newStudentsArr:
        print(student[1], student[2], student[0])
