a, b, c = list(map(int, input().split()))
x, y, z = list(map(int, input().split()))

count = (x//a) * (y//b) * (z//c)
print(count)