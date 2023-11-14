def fibonacci(n):
    f_seq = []
    a = b = 1
    count = 0
    while count < n:
        v = a + b
        if v % 3 == 0 or str(v).count('3') > 0:
            f_seq.append(v)
            count += 1
        a = b
        b = v
    return f_seq
    
f_seq = fibonacci(60)

while True:
    try:
        n = int(input())
        print(f_seq[n-1])
    except:
        break