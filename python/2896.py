n = int(input())

for i in range(n):
    n, m = input().split()
    n = int(n)
    m = int(m)
    
    bottles = n % m
    bottles += int(n / m) 
    print(bottles)