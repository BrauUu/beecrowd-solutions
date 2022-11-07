n = int(input())

numbers = input().split()
numbersInt = []
res = 0

for i in range(n):
    numbersInt.append(int(numbers[i]))
   
if n > 2:
    for i in range(n - 2):
        if numbersInt[i] > numbersInt[i + 1]:
            if numbersInt[i + 1] < numbersInt[i + 2]:
                res = 1
            else: 
                res = 0
                break
        elif numbersInt[i] < numbersInt[i + 1]:
            if numbersInt[i + 1] > numbersInt[i + 2]:      
                res = 1
            else: 
                res = 0
                break
        else:
            res = 0
            break
else:
    if numbersInt[0] > numbersInt[1] or numbersInt[0] < numbersInt[1]:
        res = 1
        
print(res)
    