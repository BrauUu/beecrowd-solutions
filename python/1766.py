t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    l = []
    for g in range(n):
        name, weight, age, height = input().split()
        l.append((name, int(weight), int(age), float(height)))
        
    l = sorted(l, key=lambda x : (x[2], x[3], x[0]))
    l = sorted(l, key=lambda x : x[1], reverse=True)
    
    print('CENARIO {' + str(i + 1) + '}')
    for g in range(len(l[:m])):
        name = l[g][0]
        print(f'{g+1} - {name}')