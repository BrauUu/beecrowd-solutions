b = int(input())
t = int(input())


leftSideArea = 0

if b > t:
    rectangleArea = t * 70    
    triangleArea = (b - t) * 70 / 2
    leftSideArea = rectangleArea + triangleArea
elif t >= b:
    rectangleArea = b * 70    
    triangleArea = (t - b) * 70 / 2
    leftSideArea = rectangleArea + triangleArea
    
if leftSideArea > 5600:
    print(1)
elif leftSideArea < 5600:
    print(2)
else:
    print(0)
    
    
    