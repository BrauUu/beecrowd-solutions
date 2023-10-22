germanyAvg = 90 / 7
brazilAvg = 90

while True:
    n = int(input())
    
    if n == 0:
        break
    
    print(f'Brasil {int(n/brazilAvg)} x Alemanha {int((n/germanyAvg) + 0.999)}')
    