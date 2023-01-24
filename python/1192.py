n = int(input())

for i in range(n):
    x = input()
    
    x0 = int(x[0])
    x1 = str(x[1])
    x2 = int(x[2])
    
    if x0 == x2:
       print(x0 * x2) 
    else:
        if x1.isupper() == True:
            print(x2 - x0)
        elif x1.islower() == True:
            print(x2 + x0)