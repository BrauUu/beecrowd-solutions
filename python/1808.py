x = input()
count = 0
sum = 0

n = len(x)
i = 0

while i < n:
    if x[i] == '1' and i < n -1 and x[i+1] == '0':
        sum += 10
        i += 2
    else:
        sum += int(x[i])
        i += 1
    count += 1
    
print(f'{sum/count:.2f}')