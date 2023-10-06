n = int(input())

for i in range(n):
    k, *_ = list(map(int, input().split()))
    sum = 0
    # for item in kItens:
    #     sum += item
    print(sum-(k-1))