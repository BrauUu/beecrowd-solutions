initialTime, endTime = input().split()
initialTime = int(initialTime)
endTime = int(endTime)

totalTime = 0

if endTime < initialTime :
    totalTime = (24 - initialTime) + endTime
elif endTime == initialTime:
    totalTime = 24
else:
    totalTime = endTime - initialTime
    
print(f'O JOGO DUROU {totalTime} HORA(S)')