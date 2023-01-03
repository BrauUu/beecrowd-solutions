n = int(input())

lose = False
carlosVotes = 0

for i in range(n):
    
    x = int(input())
    
    if i == 0:
        carlosVotes = x
    else:
        if x > carlosVotes:
            lose = True
            
print('S' if lose == False else 'N')
    