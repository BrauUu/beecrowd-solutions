n = int(input())

products = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}

sum = 0

for i in range(n):
    x = input().split()
    id = int(x[0])
    n = int(x[1])
    sum += products[id] * n

print(f'{sum:.2f}')