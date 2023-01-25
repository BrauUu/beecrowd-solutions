n = int(input())

totalWeight = 0
totalCost = 0

for i in range(n):
    dailyCost = float(input())
    fruitsArr = input().split()
    
    totalCost += dailyCost
    totalWeight += len(fruitsArr)
    
    print(f'day {i+1}: {len(fruitsArr)} kg')
    
print(f'{totalWeight / n :.2f} kg by day')
print(f'R$ {totalCost / n :.2f} by day')