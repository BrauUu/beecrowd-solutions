y = int(input())
x = int(input())

halfCount = 0
integerCount = 0

halfCount += (y - 1) * 2    
halfCount += (x - 1) * 2       

integerCount += (y * x) + ((y - 1) * (x - 1))
    
print(integerCount)
print(halfCount)