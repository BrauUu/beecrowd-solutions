x = int(input())
sumArr = []

for y in range(x):
    number1, number2 = input().split()
    sumArr.append(int(number1))
    sumArr.append(int(number2))
    
for y in range(0, len(sumArr), 2):
    try:
        print(f'{(sumArr[y] / sumArr[y+1]):.1f}')
    except:
        print('divisao impossivel')
    