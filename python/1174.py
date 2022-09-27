arr = []
rng = 100

for i in range(rng):
    arr.append(float(input()))

for i in range(rng):
    if arr[i] <= 10:
        print(f'A[{i}] = {arr[i]:.1f}')