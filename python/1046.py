initialTime, endTime = input().split()
initialTime = int(initialTime)
endTime = int(endTime)

totalTime = 0

if endTime < initialTime :
    if initialTime <= 12:
        totalTime = (12 - initialTime) + endTime
    elif initialTime > 12:
        totalTime = (24 - initialTime) + endTime
elif endTime == initialTime:
    totalTime = 24
else:
    totalTime = endTime - initialTime
    
print(f'O JOGO DUROU {totalTime} HORA(S)')