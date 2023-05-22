y = 1
while True:
    n = int(input())
    
    if n == 0:
        break

    studentsArr = []

    for i in range(n):
        name = input()
        color, size = input().split()
        
        student = {
            'name' : name,
            'color' : color,
            'size' : size
        }
        
    
        
    
    
    if y > 1:
        print()
    y += 1
    for student in studentsArr:
        print(student['color'] , student['size'] , student['name'])