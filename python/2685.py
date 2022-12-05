while True:
    try:
        angle = int(input())
        if angle >= 0 and angle < 90 or angle == 360:
            print('Bom Dia!!')
        if angle >= 90 and angle < 180:
            print('Boa Tarde!!')
        if angle >= 180 and angle < 270:
            print('Boa Noite!!')
        if angle >= 270 and angle < 360:
            print('De Madrugada!!')
    except:
        break