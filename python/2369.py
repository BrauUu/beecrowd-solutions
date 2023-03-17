x = int(input())

value = 7

if x > 100:
    value += 5 * (x - 100)
    x = 100
if x > 30:
    value += 2 * (x - 30)
    x = 30
if x > 10:
    value += (x - 10)
    x = 10

print(value)