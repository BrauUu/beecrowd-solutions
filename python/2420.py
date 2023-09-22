def fillPrefixSum(arr, n, prefixSum):
    prefixSum[0] = arr[0]
    
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]

n = int(input())

l = list(map(int, input().split()))

prefixSum = [0 for i in range(n)]
fillPrefixSum(l, n, prefixSum)

lp = prefixSum[-1]
m = prefixSum.index(int(lp/2))

print(m + 1)

