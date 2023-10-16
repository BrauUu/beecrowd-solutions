n = int(input())

for i in range(n):
    x = input()
    count = 0
    flag = False
    for letter in x.lower():
        if letter not in ['a', 'e', 'i', 'o', 'u']:
            count += 1
        else:
            count = 0
            
        if count == 3:
            flag = True
            break
    
    print(f'{x} eh facil' if flag == False else f'{x} nao eh facil')