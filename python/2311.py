n = int(input())

for i in range (n):
    name = input()
    difficult = float(input())
    
    grades = input().split()
    numberGrades = []
    
    for grade in grades:
        numberGrades.append(float(grade))
        
    numberGrades.sort()
    
    numberGrades.pop(0)
    numberGrades.pop(len(numberGrades) - 1)
    
    sum = 0
    
    for grade in numberGrades:
        sum += grade
        
    result = sum * difficult
    
    print(f'{name} {result:.2f}')
    
    
        