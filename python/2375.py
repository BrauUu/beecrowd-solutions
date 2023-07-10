n = int(input())

a, l, p = list(map(int, input().split()))

if a < n or l < n or p < n:
   print('N')
else:
   print('S')