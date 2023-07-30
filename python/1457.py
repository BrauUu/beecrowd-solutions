t = int(input())

for i in range(t):
    x = input()
    n = 0
    k = 0
    for g in range(len(x)):
        if x[g].isnumeric() == False:
            n = x[:g]
            k = len(x) - len(n)
            n = int(n)
            break
    sum = 1
    while n > 0:
       sum *= n
       n -= k   
    print(sum)