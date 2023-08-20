n = int(input())

for i in range(n):
    c1, c2 = input().split('k')
    print(f'k{(c1.count("a") * c2.count("a"))*"a"}')