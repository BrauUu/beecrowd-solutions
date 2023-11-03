n, m = list(map(int, input().split()))

dic = {}

for _ in range(n):
    e, s = input().split()
    dic[s] = e
    dic[e] = s
    
for _ in range(m):
    m = input()
    res = ''
    for letter in m:
        res += dic.get(letter) or letter
    print(res)