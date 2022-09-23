_, startDay = input().split()
startTime = input().split(" : ")
_, endDay = input().split()
endTime = input().split(" : ")

startDay = int(startDay)

endDay = int(endDay)

startHour = int(startTime[0])
startMinutes = int(startTime[1])
startSeconds = int(startTime[2])

endHour = int(endTime[0])
endMinutes = int(endTime[1])
endSeconds = int(endTime[2])

totalDays = 0
totalHours = 0
totalMinutes = 0
totalSeconds = 0

totalDays = endDay - startDay

if endHour > startHour or (endHour == startHour and endMinutes > startMinutes) or (endHour == startHour and endMinutes == startMinutes and endSeconds > startSeconds):
    totalHours = endHour - startHour
    totalMinutes = endMinutes - startMinutes
    totalSeconds = endSeconds - startSeconds

if endHour < startHour:
    totalDays -= 1
    totalHours = 24 - (startHour - endHour)
else: 
    totalHours = endHour - startHour
    
if endMinutes < startMinutes:
    if totalHours <= 0:
        totalDays -= 1
        totalHours = 24 - (totalHours) -1
    else:
        totalHours -= 1
    totalMinutes =  60 - (startMinutes - endMinutes)
else:
    totalMinutes =  endMinutes - startMinutes
    
if endSeconds < startSeconds:
    if totalMinutes <= 0:
        totalHours -= 1
        totalMinutes = 60 - (totalMinutes) - 1
    else:
        totalMinutes -= 1
    totalSeconds = 60 - (startSeconds - endSeconds)
else:
    totalSeconds = endSeconds - startSeconds
    
print(f'{totalDays} dia(s)')
print(f'{totalHours} hora(s)')
print(f'{totalMinutes} minuto(s)')
print(f'{totalSeconds} segundo(s)')