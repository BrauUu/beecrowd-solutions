n = int(input())

for i in range(n):
    diet = input()
    food = input()
    food += input()
    
    flag = False
    dietCopy = [x for x in diet]
    
    for item in food:
        if dietCopy.count(item) > 0:
            ind = dietCopy.index(item)
            dietCopy = dietCopy[:ind] + dietCopy[ind + 1:]
        else:
            flag = True
            break
        
    dietCopy.sort()
    
    if flag == True:
        print('CHEATER')
    else:
        print(''.join(dietCopy))