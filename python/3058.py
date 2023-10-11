n = int(input())

lowest = 0

for i in range(n):
    v, g = list(map(float, input().split()))
    p = v * (1000/g)
    if i == 0:
        lowest = p
    elif p < lowest:
        lowest = p
    
print(f'{lowest:.2f}')
    