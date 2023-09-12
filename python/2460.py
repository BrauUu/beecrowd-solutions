n = int(input())
l = list(map(int, input().split()))
m = int(input())
r = list(map(int, input().split()))

for i in r:
    try:
        l.remove(i)
    except:
        None

res = ''

for i in l:
    res += str(i) + ' '
    
print(res.strip())