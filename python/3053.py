n = int(input())

actualPos = input()

for i in range(n):
    move = int(input())
    
    if move == 1:
        if actualPos == 'A' or actualPos == 'B':
            actualPos = 'A' if actualPos == 'B' else 'B'
    elif move == 2:
        if actualPos == 'B' or actualPos == 'C':
            actualPos = 'B' if actualPos == 'C' else 'C'
    elif move == 3:
        if actualPos == 'A' or actualPos == 'C':
            actualPos = 'A' if actualPos == 'C' else 'C'
        
print(actualPos)
            