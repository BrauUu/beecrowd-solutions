def paperAndScissors(p1, p2):
    if p1 == 'tesoura':
        if p2 == 'papel':
            return 1
        elif p2 == 'pedra':
            return 2
        elif p2 == 'tesoura':
            return 0
    elif p1 == 'papel':
        if p2 == 'papel':
            return 0
        elif p2 == 'pedra':
            return 1
        elif p2 == 'tesoura':
            return 2
    elif p1 == 'pedra':
        if p2 == 'papel':
            return 2
        elif p2 == 'pedra':
            return 0
        elif p2 == 'tesoura':
            return 1
    

while True:
    try:
        p1, p2, p3 = input().split()
        
        win1 = paperAndScissors(p1, p2)
        finalWin = ''
        
        if p1 != p2 and p2 != p3 and p1 != p3:
            print('Putz vei, o Leo ta demorando muito pra jogar...')
        elif win1 == 1:
            finalWin = paperAndScissors(p1, p3)
            if finalWin == 1:
                print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
            elif finalWin == 2:
                print("Urano perdeu algo muito precioso...")
            elif finalWin == 0:
                print('Putz vei, o Leo ta demorando muito pra jogar...')
        elif win1 == 2:
            finalWin = paperAndScissors(p2, p3)
            if finalWin == 1:
                print("Iron Maiden's gonna get you, no matter how far!")
            elif finalWin == 2:
                print("Urano perdeu algo muito precioso...")
            elif finalWin == 0:
                print('Putz vei, o Leo ta demorando muito pra jogar...')
        elif win1 == 0:
            finalWin = paperAndScissors(p2, p3)
            if finalWin == 1 or finalWin == 0:
                print('Putz vei, o Leo ta demorando muito pra jogar...')
            elif finalWin == 2:
                print("Urano perdeu algo muito precioso...")
           
    except:
        break