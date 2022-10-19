while True:
    try:
        hour, minutes = input().split(':')
        hour = int(hour)
        minutes = int(minutes)

        minutes += 60
        lateH = 0
        lateM = 0

        if minutes >= 60:
            hour += 1
            minutes -= 60

        if hour >= 8:
            lateH = hour - 8
            lateM = minutes

        late = (lateH * 60) + lateM

        print(f'Atraso maximo: {late}')
    except:
        break
