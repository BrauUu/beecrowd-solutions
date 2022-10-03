gamesCount = 0
gremioWins = 0
interWins = 0
drawsCount = 0

while True:
    goals = input().split()
    
    gremioGoals = int(goals[1])
    interGoals = int(goals[0])
    
    if gremioGoals > interGoals:
        gremioWins += 1
    elif interGoals > gremioGoals:
        interWins += 1
    else:
        drawsCount += 1
        
    gamesCount += 1
    
    print('Novo grenal (1-sim 2-nao)')
    x = int(input())
    
    if x == 2:
        break
        
print(f'{gamesCount} grenais')
print(f'Inter:{interWins}')
print(f'Gremio:{gremioWins}')
print(f'Empates:{drawsCount}')

if gremioWins > interWins:
    print('Gremio venceu mais')
elif gremioWins < interWins:
    print('Inter venceu mais')
else:
    print('Nao houve vencedor')