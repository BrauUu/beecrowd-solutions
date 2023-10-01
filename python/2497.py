i = 1
while True:
    n = int(input())
    if n == -1:
        break    
    print(f'Experiment {i}: {int(n/2)} full cycle(s)')
    i += 1