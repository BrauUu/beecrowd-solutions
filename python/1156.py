sum = 1
x = 2
count = 1

for i in range(3, 40, 2):
  sum += round((i / pow(x, count)))
  count += 1
  
print(f'{sum:.2f}')

    