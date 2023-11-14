l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l1.sort()
l2.sort()

if l1[0] <= l2[0] and l1[1] <= l2[1]:
    print('S')
else:
    print('N')