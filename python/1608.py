t = int(input())

for i in range(t):
    d, i, b = list(map(int, input().split()))
    iList = list(map(int, input().split()))
    pList = []
    for j in range(b):
        qis, *l = list(map(int, input().split()))
        p = 0
        for g in range(0, qis * 2, 2):
            p += iList[l[g]] * l[g+1]
        pList.append(p)
    pList.sort()
    print(d//pList[0])