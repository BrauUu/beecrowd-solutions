age = int(input())

years = age/365
months = (age % 365) / 30
days = ((age % 365) % 30)

print(int(years), "ano(s)")
print(int(months), "mes(es)")
print(int(days), "dia(s)")