n = int(input())
mineField = []

for i in range(n):
    mineField.append(int(input()))

for i in range(len(mineField)):
    count = 0
    if mineField[i] == 1:
        count += 1    
    if i > 0 and mineField[i-1] == 1:
        count +=1 
    if i < len(mineField) - 1 and mineField[i+1] == 1:
        count += 1
    print(count)
