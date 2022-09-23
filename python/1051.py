salary = float(input())
tax = 0
actualValue = salary

if actualValue > 4500:
    appliedValue = actualValue - 4500
    tax += appliedValue * 28 / 100
    actualValue -= appliedValue
if actualValue > 3000 and actualValue <= 4500:
    appliedValue = actualValue - 3000
    tax += appliedValue * 18 / 100
    actualValue -= appliedValue
if actualValue > 2000 and actualValue <= 3000:
    appliedValue = actualValue - 2000
    tax += appliedValue * 8 / 100
    actualValue -= appliedValue
if salary < 2000:
    print('Isento')
else:
    print(f'R$ {tax:.2f}')
