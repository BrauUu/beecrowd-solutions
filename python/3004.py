n = int(input())

for _ in range(n):
    e1l1, e1l2, e2l1, e2l2 = list(map(int, input().split()))
    e1b, e1s = (e1l1, e1l2) if e1l1 > e1l2 else (e1l2, e1l1)
    e2b, e2s = (e2l1, e2l2) if e2l1 > e2l2 else (e2l2, e2l1)
    
    print('S' if e1b < e2b and e1s < e2s else 'N')