n = int(input())

chosen = {
    'reg': '',
    'grade': 0
}

for i in range(n):
    
    reg, grade = input().split()
    grade = float(grade)
    
    if grade >= 8 and grade > chosen['grade']: 
        chosen['reg'] = reg
        chosen['grade'] = grade
        
if chosen['reg'] != '':
    print(chosen['reg'])
else:
    print('Minimum note not reached')