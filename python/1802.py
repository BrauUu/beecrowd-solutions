p, *pList = list(map(int, input().split()))
m, *mList = list(map(int, input().split()))
f, *fList = list(map(int, input().split()))
q, *qList = list(map(int, input().split()))
b, *bList = list(map(int, input().split()))
n =int(input())

sumList = []

for pv in pList:
    for mv in mList:
        for fv in fList:
            for qv in qList:
                for bv in bList:
                    sum = pv + mv + fv + qv + bv
                    sumList.append(sum)

sumList.sort(reverse=True) 
res = 0        
for i in range(n):
    res += sumList[i]
    
print(res)