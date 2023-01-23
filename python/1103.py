while True:
    h1, m1, h2, m2 = input().split()
    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)
    
    if h1 == m1 == h2 == m2 == 0:
        break
    
    totalTime = 0
    
    hours = h2 - h1
    if hours < 0:
        hours = 24 + hours
    minutes = m2 - m1
    if minutes < 0:
        minutes = 60 + minutes
        hours = hours - 1 if hours > 0 else 23
    totalTime = hours * 60 + minutes
        
        
    print(totalTime)