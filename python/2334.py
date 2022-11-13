while True:
    ducks = int(input())
    
    if ducks == -1:
        break
    
    if ducks - 1 > 0:
        print(ducks - 1)
    else:
        print(0)