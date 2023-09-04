c = int(input())
for i in range(c):
    # Red, Green, Blue
    r = {'points': 0, 'hourly': 'g', 'antihourly': 'b'}
    g = {'points': 0, 'hourly': 'b', 'antihourly': 'r'}
    b = {'points': 0, 'hourly': 'r', 'antihourly': 'g'}
    p = int(input())
    for h in range(p):
        m, s = input().split()
        m = m.lower()
        s = s.lower()
        eval(m)['points'] += 2 if eval(m)['hourly'] == eval(f"'{s}'") else 1  
    
    winner = ''
    
    if r['points'] > g['points'] and r['points'] > b['points']:
        winner = 'red'
    elif g['points'] > r['points'] and g['points'] > b['points']:
        winner = 'green'
    elif b['points'] > r['points'] and b['points'] > g['points']: 
        winner = 'blue'
    
    if winner:
        print(winner)
    elif r['points'] == g['points'] and r['points'] == b['points'] and g['points'] == b['points']:
        print('trempate')
    else:
        print('empate')
        