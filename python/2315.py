from datetime import date, timedelta

d1, m1 = list(map(int, input().split()))
d2, m2 = list(map(int, input().split()))

date1 = date(1, m1, d1)
date2 = date(1, m2, d2)

print(f'{(str(date2 - date1).split()[0]).split(":")[0]}')