n = int(input())

total = 0
rabbitsTotal = 0
ratsTotal = 0
frogsTotal = 0

for i in range(n):
    qty, tp = input().split()
    qty = int(qty)
    
    if tp == 'C':
        rabbitsTotal += qty
    elif tp == 'R':
        ratsTotal += qty
    elif tp == 'S':
        frogsTotal += qty
        
    total += qty
    
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {rabbitsTotal}')
print(f'Total de ratos: {ratsTotal}')
print(f'Total de sapos: {frogsTotal}')
print(f'Percentual de coelhos: {(rabbitsTotal * 100 / total):.2f} %')
print(f'Percentual de ratos: {(ratsTotal * 100 / total):.2f} %')
print(f'Percentual de sapos: {(frogsTotal * 100 / total):.2f} %')
    