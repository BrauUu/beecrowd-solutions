initialHour, initialMinutes, endHour, endMinutes = input().split()
initialHour = int(initialHour)
initialMinutes = int(initialMinutes)
endHour = int(endHour)
endMinutes = int(endMinutes)

totalHours = 0
totalMinutes = 0

if endHour < initialHour :
    totalHours = (24 - initialHour) + endHour
elif endHour == initialHour:
    totalHours = 24
else:
    totalHours = endHour - initialHour
    
if endMinutes > initialMinutes:
    if endHour == initialHour:
        totalHours = 0
    totalMinutes = endMinutes - initialMinutes
elif initialMinutes > endMinutes:
    totalHours -= 1;
    totalMinutes = 60 - (initialMinutes - endMinutes)
    
print(f'O JOGO DUROU {totalHours} HORA(S) E {totalMinutes} MINUTO(S)')