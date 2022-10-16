qt = int(input())

for i in range(qt):
    playersAndChoices = input().split()

    player1 = playersAndChoices[0]
    player2 = playersAndChoices[2]
    player1Choice = playersAndChoices[1]
    player2Choice = playersAndChoices[3]

    values = input().split()
    player1Value = int(values[0])
    player2Value = int(values[1])

    if (player1Value + player2Value) % 2 == 0:
        if player1Choice == 'PAR':
            print(player1)
        elif player2Choice == 'PAR':
            print(player2)
    elif (player1Value + player2Value) % 2 == 1:
        if player1Choice == 'IMPAR':
            print(player1)  
        elif player2Choice == 'IMPAR':
            print(player2)
            
    