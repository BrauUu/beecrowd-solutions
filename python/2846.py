n = int(input())

fib = [1, 1]
count = 0
res = 0
flag = False

for i in range(2, 10000):
    fib.append(fib[i-2] + fib[i-1])
    for g in range(fib[i-2] + 1, fib[i-1]):
        if fib[i-2] != fib[i-1]:
            count += 1
        if count == n:
            res = g
            flag = True
    if flag == True:
        print(res)
        break

