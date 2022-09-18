value = int(input())
initialValue = value

count100Bills = int(value / 100)
value = value - count100Bills * 100
count50Bills =  int(value / 50)
value = value - count50Bills * 50
count20Bills =  int(value / 20)
value = value - count20Bills * 20
count10Bills =  int(value / 10)
value = value - count10Bills * 10
count5Bills =  int(value / 5)
value = value - count5Bills * 5
count2Bills =  int(value / 2)
value = value - count2Bills * 2
count1Bills =  int(value / 1)
value = value - count1Bills * 1

print(initialValue)
print(f'{count100Bills} nota(s) de R$ 100,00')
print(f'{count50Bills} nota(s) de R$ 50,00')
print(f'{count20Bills} nota(s) de R$ 20,00')
print(f'{count10Bills} nota(s) de R$ 10,00')
print(f'{count5Bills} nota(s) de R$ 5,00')
print(f'{count2Bills} nota(s) de R$ 2,00')
print(f'{count1Bills} nota(s) de R$ 1,00')