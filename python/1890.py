n = int(input())

for i in range(n):
    c, d = list(map(int, input().split()))
    
    if c == d == 0:
        print(0)
        continue
    
    print(26 ** c * 10 ** d)