n = int(input())

la, lb = list(map(int, input().split()))
sa, sb = list(map(int, input().split()))

if n <= lb and n >= la and n <= sb and n >= sa:
    print('possivel')
else:
    print('impossivel')