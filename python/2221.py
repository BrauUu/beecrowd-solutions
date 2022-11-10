x = int(input())

def calcHitvalue(attack, defense, level, bonus):
    return (attack + defense) / 2 + (bonus if level % 2 == 0 else 0)
     

for i in range(x):
        
        bonus = int(input())
        
        attackDabriel, defenseDabriel, levelDabriel = input().split()
        attackDabriel = int(attackDabriel)
        defenseDabriel= int(defenseDabriel)
        levelDabriel = int(levelDabriel)
        
        attackGuarte, defenseGuarte, levelGuarte = input().split()
        attackGuarte = int(attackGuarte)
        defenseGuarte= int(defenseGuarte)
        levelGuarte = int(levelGuarte)
        
        hitValueDabriel = calcHitvalue(attackDabriel, defenseDabriel, levelDabriel, bonus)
        hitValueGuarte = calcHitvalue(attackGuarte, defenseGuarte, levelGuarte, bonus)
    
        if hitValueDabriel > hitValueGuarte:
            print('Dabriel')
        elif hitValueGuarte > hitValueDabriel:
            print('Guarte')
        else:
            print('Empate')
    