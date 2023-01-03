n = int(input())

aCount = 0
eCount = 0
hCount = 0
mCount = 0
xCount = 0

for i in range(n):
    name, race = input().split()
    
    if race == 'A':
        aCount +=1
    elif race == 'E':
        eCount +=1
    elif race == 'H':
        hCount +=1
    elif race == 'M':
        mCount +=1
    elif race == 'X':
        xCount +=1
        
print(f'{xCount} Hobbit(s)')
print(f'{hCount} Humano(s)')
print(f'{eCount} Elfo(s)')
print(f'{aCount} Anao(oes)')
print(f'{mCount} Mago(s)')
