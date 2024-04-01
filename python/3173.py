from datetime import date, timedelta

n = int(input())

bj = round(11.9*n/4)
jDate = date(2020, 12, 21)
jDays = 11.9 * n * 365 + bj


bs = int(29.6*n/4)
sDate = date(2020, 12, 21)
sDays = 29.6 * n * 365 + bs

jDate = jDate + timedelta(jDays)
sDate = sDate + timedelta(sDays)

print(f'Dias terrestres para Jupiter = {int(jDays)}')
print(f'Data terrestre para Jupiter: {jDate}')
print(f'Dias terrestres para Saturno = {int(sDays)}')
print(f'Data terrestre para Saturno: {sDate}')