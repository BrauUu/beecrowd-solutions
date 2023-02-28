def fat(x):
    if x <= 1:
        return 1
    else:
        return x * fat(x-1)

while True:
    try:
        n, m = list(map(int, input().split()))
        
        sum = fat(n) + fat(m)     
        
        print(sum)
           
    except:
        break