x = int(input())

wrestAttempts = 0
wrestHits = 0
blockAttempts = 0
blockHits = 0
attackAttempts = 0
attackHits = 0

for i in range(x):
    name = input()
    
    attempts = input().split()
    hits = input().split()
    
    wrestAttempts += int(attempts[0])
    wrestHits += int(hits[0])
    blockAttempts += int(attempts[1])
    blockHits += int(hits[1])
    attackAttempts += int(attempts[2])
    attackHits += int(hits[2])
    
print(f'Pontos de Saque: {(wrestHits * 100 / wrestAttempts):.2f} %.')
print(f'Pontos de Bloqueio: {(blockHits * 100 / blockAttempts):.2f} %.')
print(f'Pontos de Ataque: {(attackHits * 100 / attackAttempts):.2f} %.')
    
    
    