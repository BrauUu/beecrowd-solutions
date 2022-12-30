n = int(input())

for i in range(n):
    n, m = input().split()
    
    x = len(str(pow(int(n),int(m))))
    print(x)