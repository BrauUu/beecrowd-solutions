n = int(input())

countriesList = []

for i in range(n):
    country, goldMedals, silverMedals, bronzeMedals = input().split()
    countriesList.append((country, int(goldMedals), int(silverMedals), int(bronzeMedals)))
    
countriesList = sorted(countriesList, key=lambda item: item[0])
countriesList = sorted(countriesList, key=lambda item: (item[1], item[2], item[3]), reverse=True)

for country in countriesList:
    print(f'{country[0]} {country[1]} {country[2]} {country[3]}')