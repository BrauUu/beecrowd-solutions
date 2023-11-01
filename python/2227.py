count = 1
while True:
    a, v = list(map(int, input().split()))
    if a == v == 0:
        break
    
    airportsFlights = {}
    for i in range(1, a + 1):
        airportsFlights[i] = 0
            
    for i in range(v):
        x, y = list(map(int, input().split()))
        airportsFlights.update({x: (int(airportsFlights.get(x) or 0) + 1)})
        airportsFlights.update({y: (int(airportsFlights.get(y) or 0) + 1)})
    
    bigger = 0
    res = ''
    
    for key, v in airportsFlights.items():
        if v > bigger:
            res = str(key) + ' '
            bigger = v
        elif v == bigger:
            res += str(key) + ' '
       
    print(f'Teste {count}')           
    print(res)
    print()
    count += 1