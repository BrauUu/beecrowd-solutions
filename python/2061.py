pgNumber, actionsNumber = input().split()

pgNumber = int(pgNumber)
actionsNumber = int(actionsNumber)

for i in range(actionsNumber):
    action = input()
    
    if action == 'fechou':
        pgNumber += 1
    elif action == 'clicou':
        pgNumber -= 1
        
print(pgNumber)