def eyesValue(value):
    sum = 0
    if value[0] == "*":
        sum += 4
    if value[1] == "*":
        sum += 2
    if value[2] == "*":
        sum += 1
    return sum

count = 0
sum = 0

numbers = []

while True:
    x = input()
    if x == "caw caw":
        count +=1
        numbers.append(sum)
        sum = 0
    else:
        sum += eyesValue(x)
    if count == 3:
        break
    
for number in numbers:
    print(number)