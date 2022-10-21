while True:
    try:
        volume = float(input())
        diameter = float(input())
        PI = 3.14
        
        radius = diameter / 2
        
        baseArea = pow(radius, 2) * PI
        height = volume / baseArea
        
        print(f'ALTURA = {height:.2f}')
        print(f'AREA = {baseArea:.2f}')
        
    except:
        break