while True:
    try:
        angle = float(input())
        greetings = ''
        
        seconds = (angle * 240 ) + 21600 if angle <= 270 else (angle * 240) - 64800
        
        hour = int(seconds / 3600)
        remainingSeconds = seconds - hour * 3600
        minutes = int(remainingSeconds / 60)
        remainingSeconds = remainingSeconds - minutes * 60
        seconds = int(remainingSeconds)
        
        hour = hour if hour < 24 else hour - 24
        minutes = minutes if minutes < 60 else minutes - 60
        seconds = seconds if seconds < 60 else seconds - 60
        
        hour = str(hour) if hour >= 10 else '0' + str(hour)
        minutes = str(minutes) if minutes >= 10 else '0' + str(minutes)
        seconds = str(seconds) if seconds >= 10 else '0' + str(seconds)
        
        time = f'{hour}:{minutes}:{seconds}'
        
        if angle >= 0 and angle < 90 or angle == 360:
            greetings = 'Bom Dia!!'
        if angle >= 90 and angle < 180:
            greetings = 'Boa Tarde!!'
        if angle >= 180 and angle < 270:
            greetings = 'Boa Noite!!'
        if angle >= 270 and angle < 360:
            greetings = 'De Madrugada!!'
            
        print(greetings)
        print(time)
    except:
        break
   