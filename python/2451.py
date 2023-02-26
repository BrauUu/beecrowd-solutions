n = int(input())

largestAmountOfFood = 0
foodAmount = 0

start = 0
end = 0
step = 1

for i in range(n):
    
    maze = input()
    
    if i % 2 == 0:
        start = 0
        end = n
        step = 1
    else:
        start = n - 1
        end = -1
        step = -1
        
    for g in range(start, end, step):

        if maze[g] == 'o':
            foodAmount += 1
        elif maze[g] == 'A':
            if foodAmount > largestAmountOfFood:
                largestAmountOfFood = foodAmount
            foodAmount = 0
            
    if foodAmount > largestAmountOfFood:
        largestAmountOfFood = foodAmount
            
print(largestAmountOfFood)