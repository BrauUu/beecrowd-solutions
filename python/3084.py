while True:
    try:
       h, m = input().split()
       h = int(h)       
       m = int(m)  
       
       hours = int(h / 30)
       minutes = int((m / 30) * 5)
       
       hours = hours if hours >= 10 else '0'+ str(hours)
       minutes = minutes if minutes >= 10 else '0'+ str(minutes)
       
       print(f'{hours}:{minutes}')
            
    except:
        break