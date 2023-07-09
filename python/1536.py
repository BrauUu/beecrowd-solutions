n = int(input())

for i in range(n):
    team1 = {
        'points' : 0,
        'goalsOut' : 0,
        'goalsBalance' : 0,
    }
    
    team2 = {
        'points' : 0,
        'goalsOut' : 0,
        'goalsBalance' : 0,
    }
    
    cGoals, vGoals = list(map(int, input().split(' x ')))
    
    res = cGoals - vGoals
    
    if res > 0:
        team1['points'] += 3
    elif res < 0:
        team2['points'] += 3
    else:
        team1['points'] += 1
        team2['points'] += 1
      
    team1['goalsBalance'] += res
    team2['goalsBalance'] += -res
    
    team2["goalsOut"] += vGoals
    
    cGoals, vGoals = list(map(int, input().split(' x ')))
    
    res = cGoals - vGoals
    
    if res > 0:
        team2['points'] += 3
    elif res < 0:
        team1['points'] += 3
    else:
        team1['points'] += 1
        team2['points'] += 1
      
    team2['goalsBalance'] += res
    team1['goalsBalance'] += -res
    
    team1["goalsOut"] += vGoals
    
    result = ''
    
    if team1["points"] > team2["points"]:
        result = 'Time 1'
    elif team1["points"] < team2["points"]:
        result = 'Time 2'
    else:
        if team1["goalsBalance"] > team2["goalsBalance"]:
            result = 'Time 1'
        if team1["goalsBalance"] < team2["goalsBalance"]:
            result = 'Time 2'       
        else:
            if team1["goalsOut"] > team2["goalsOut"]:
                result = 'Time 1'
            elif team1["goalsOut"] < team2["goalsOut"]:
                result = 'Time 2'
            else:
                result = 'Penaltis'
                
    print(result)