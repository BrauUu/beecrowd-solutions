while True:
    try:
        x = int(input())
        print("Y" if x % 6 == 0 else "N")        
    except:
        break