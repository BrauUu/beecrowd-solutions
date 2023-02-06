n = int(input())

for i in range(n):
    x = input()
    
    start = x.find('<')
    end = x.rfind('>') + 1
    x1 = x[:end].count('<')
    x2 = x[start:].count('>')
    if x1 < x2:
        print(x1)
    else:
        print(x2)
       