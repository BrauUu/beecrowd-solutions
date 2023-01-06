m = int(input())
a = int(input())
b = int(input())

x = m - (a + b)

print(x if x > a and x > b else a if a > b else b)