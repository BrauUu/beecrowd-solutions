while True:
    try:
        x, y, z = list(map(int, input().split()))
        
        if x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or z**2 + y**2 == x**2:
            anterior = x
            atual = y
            resto = anterior % atual

            while resto != 0:
                anterior = atual
                atual = resto
                resto = anterior % atual
            if atual == 1:
                print('tripla pitagorica primitiva')        
            else:  
                print('tripla pitagorica')
        else:
            print('tripla')
    except:
        break