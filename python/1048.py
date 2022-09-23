salary = float(input())

percentage = 0

if salary <= 400:
    percentage = 15
elif salary > 400 and salary <= 800:
    percentage = 12
elif salary > 800 and salary <= 1200:
    percentage = 10
elif salary > 1200 and salary <= 2000:
    percentage = 7 
elif salary > 2000:
    percentage = 4 
    
addition = (salary * percentage / 100)
newSalary = salary + addition
print(f'Novo salario: {newSalary:.2f}')
print(f'Reajuste ganho: {addition:.2f}')
print(f'Em percentual: {percentage} %')