n = int(input())

for i in range(n):
    p1Choice = input()
    p2Choice = input()
    
    if p1Choice == 'ataque' and p2Choice != 'ataque':
        print('Jogador 1 venceu')
    elif p2Choice == 'ataque' and p1Choice != 'ataque':
        print('Jogador 2 venceu')
    elif p1Choice == 'pedra' and p2Choice == 'papel':
        print('Jogador 1 venceu')
    elif p2Choice == 'pedra' and p1Choice == 'papel':
        print('Jogador 2 venceu')
    elif p1Choice == 'papel' and p2Choice == 'papel':
        print('Ambos venceram')
    elif p1Choice == 'pedra' and p2Choice == 'pedra':
        print('Sem ganhador')
    elif p1Choice == 'ataque' and p2Choice == 'ataque':
        print('Aniquilacao mutua')
    