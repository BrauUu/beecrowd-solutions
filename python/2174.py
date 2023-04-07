n = int(input())

arr = []

for i in range(n):
    x = input()
    try:
        arr.index(x)
    except:
        arr.append(x)

print(f'Falta(m) {151 - len(arr)} pomekon(s).')